import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))

        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs

        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'

        output = [f"Result for '{directory}' directory:"]

        files = os.listdir(target_dir)

        for file in files:
            full_path = os.path.join(target_dir, file)
            
            file_size = os.path.getsize(full_path)
            file_is_dir = os.path.isdir(full_path)
            
            output.append(f"  - {file}: file_size={file_size} bytes, is_dir={file_is_dir}")

        return "\n".join(output)

    except Exception as e:
        return f"Error: {e}"

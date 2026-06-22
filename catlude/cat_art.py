IDLE_CAT = r"""
 ,_     _
 |\\_,-~/
 / _  _ |    ,--.
(  @  @ )   / ,-'
 \  _T_/-._( (
 /         `. \
|         _  \ |
 \ \ ,  /      |
  || |-_\__   /
 ((_/`(____,-'
"""

WORKING_CAT = r"""
 ,-.       _,---._ __  / \
 /  )    .-'       `./ /   \
(  (   ,'            `/    /|
 \  `-"             \'\   / |
  `.              ,  \ \ /  |
   /`.          ,'-`----Y   |
  (            ;        |   '
  |  ,-.    ,-'         |  /
  |  | (   |        hjw | /
  )  |  \  `.___________|/
  `--'   `--'
"""


def print_idle_cat() -> None:
    print(IDLE_CAT)
    print("CATlude — Tiny coding cat agent")
    print("=" * 34)
    print()


def print_working_cat() -> None:
    print(WORKING_CAT)
    print("*purrr* working on it...\n")

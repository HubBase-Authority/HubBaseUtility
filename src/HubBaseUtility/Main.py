from . import all_programs
from .Programs.Manager import Program
__version__ = "0.0.0.1.00"


def main():
    print(f"=== HubBaseUtility v{__version__} ===")
    for pr_id in all_programs:
        try:
            Program(pr_id).run(None)
        except ImportError as e:
            print(e)
        except Exception as e:
            print(f"Failed to run program {pr_id}: {e}")


if __name__ == '__main__':
    main()

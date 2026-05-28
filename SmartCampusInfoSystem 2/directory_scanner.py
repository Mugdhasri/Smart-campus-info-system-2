# -*- coding: utf-8 -*-
# ============================================================
# Lab 7: Directory Scanning with Exception Handling
# Smart Campus Information System
# ============================================================

import os


# ── User-defined Exception ───────────────────────────────────
class MissingFileOrFolderError(Exception):
    """Raised when a required file or folder is missing in the directory."""
    pass


# ── Core scanning function ───────────────────────────────────
def scan_directory(path):
    """
    Scan and display the folder structure of the given path.

    Args:
        path (str): Directory path to scan.
    """
    try:
        if not os.path.exists(path):
            raise FileNotFoundError(f"Invalid directory path: '{path}'")

        print(f"\nScanning directory: {os.path.abspath(path)}\n")

        for root, dirs, files in os.walk(path):
            level      = root.replace(path, "").count(os.sep)
            indent     = "    " * level
            sub_indent = "    " * (level + 1)

            print(f"{indent}{os.path.basename(root)}/")
            for f in files:
                print(f"{sub_indent}{f}")

            # User-defined exception: empty folder (no files AND no sub-dirs)
            if not files and not dirs:
                raise MissingFileOrFolderError(
                    f"Empty folder detected: {root}"
                )

    except FileNotFoundError as e:
        print(f"[FileNotFoundError] {e}")
    except MissingFileOrFolderError as e:
        print(f"[CustomError] {e}")
    except PermissionError as e:
        print(f"[PermissionError] Access denied – {e}")
    except Exception as e:
        print(f"[UnexpectedError] {e}")


def directory_scanner_module():
    """Interactive directory scanning module."""
    print("\n" + "=" * 45)
    print("     DIRECTORY SCANNER – FILE & FOLDER VIEW")
    print("=" * 45)

    # Create a sample project directory for demo purposes
    sample_path = "SampleProjects"
    os.makedirs(f"{sample_path}/Student1", exist_ok=True)
    os.makedirs(f"{sample_path}/Student2", exist_ok=True)
    os.makedirs(f"{sample_path}/EmptyFolder", exist_ok=True)

    # Create sample files
    with open(f"{sample_path}/Student1/report.docx", "w") as f:
        f.write("Sample report content")
    with open(f"{sample_path}/Student2/code.py", "w") as f:
        f.write("# Sample Python code")

    print("\n[Demo] Scanning auto-created 'SampleProjects' directory:")
    scan_directory(sample_path)

    print("\n[Demo] Scanning an invalid path:")
    scan_directory("NonExistentPath/xyz")

    # Optional: let user scan their own directory
    user_choice = input("\nScan a custom directory? (yes/no): ").strip().lower()
    if user_choice == "yes":
        custom_path = input("Enter directory path: ").strip()
        scan_directory(custom_path)


if __name__ == "__main__":
    directory_scanner_module()

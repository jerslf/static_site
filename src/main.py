import os
import shutil


def main():
    copy_directory("static", "public")


def copy_directory(src, dest):
    print(f"Copying from: {src} to {dest}")

    # Delete destination if it exists
    if os.path.exists(dest):
        shutil.rmtree(dest)
    os.makedirs(dest)

    # Recurse through files and directories
    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dest_path = os.path.join(dest, item)

        if os.path.isfile(src_path):
            shutil.copy(src_path, dest_path)
            print(f"Copied file: {src_path} -> {dest_path}")
        elif os.path.isdir(src_path):
            print(f"Creating directory: {dest_path}")
            copy_directory(src_path, dest_path)


if __name__ == "__main__":
    main()

import os
import numpy as np
import time


class FileRenameUtilities:
    def __init__(self):
        self.files_dir = [file for file in os.listdir('randompics')]
        self.valid_exts = [".jpg", ".jpeg", ".png"]
        self.new_files = self.initial_renamer()
        self.file_chosen = np.random.choice(self.files_dir)
        # print('new files:', self.new_files)

    def initial_rename_file_only(self, inputfile):
        file_modified = str(inputfile).split('.')
        return f'{file_modified[0]}(1).{file_modified[1]}'

    def initial_renamer(self):
        ''' FYI: this will rename initially all files prefixed with 1 just for testing.'''
        all_files_renamed = [f'{file.split(".")[0]}(1).{file.split(".")[-1]}' for file in self.files_dir]
        return all_files_renamed
        # print(all_files_renamed)

    def file_check(self, fileinput):
        if '(' in fileinput:
            first_elem = str(fileinput).split('(')[0]
            last_elem = str(fileinput).split('(')[1].split(')')[1]
        return fileinput

    def allot_new_name(self, file):
        first_elem = str(file).split('(')[0]
        last_elem = str(file).split('(')[1].split(')')[1]
        freq = int(file.split('(')[-1].split(')')[0])
        freq += 1
        final_name = f'{first_elem}({str(freq)}){last_elem}'
        # print('filename:', first_elem)
        # print('extension:', last_elem)
        return final_name

    def initial_trim(self):
        print(f'file taken for now: {self.file_chosen}')
        filename, ext = os.path.splitext(self.file_chosen)
        if ext in self.valid_exts:
            pass
        else:
            print("selected file is not a valid image file.".capitalize())

    def test(self):
        for file in self.files_dir:
            if file == self.file_check(file):
                if '(' in file:
                    finalname = self.allot_new_name(file)
                else:
                    print('parentheses not found')
                    finalname = self.initial_rename_file_only(file)

                folder_path = os.path.join(os.getcwd(), 'randompics')
                print('renaming...')
                time.sleep(1)
                os.rename(os.path.join(folder_path, file), os.path.join(folder_path, finalname))
                print(f'{finalname} affected successfully.')
            else:
                pass


FileRenameUtilities().test()
print('renamed')

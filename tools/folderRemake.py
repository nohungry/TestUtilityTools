import os
import shutil

DESKTOP = os.path.join(os.path.expanduser("~"), "Desktop") + "\\"

def folderRemake(name, mark=False):
    """
        name: 資料夾名稱
        mark: 是否需要重新于Desktop建立資料夾 True/ False, 預設為False
    """
    screenFolderPath = os.path.join(DESKTOP, str(name))
    if mark == True:
        if os.path.isdir(screenFolderPath):
            try:
                shutil.rmtree(screenFolderPath)
            except OSError as e:
                print(e)
            os.mkdir(screenFolderPath)
        else:
            os.mkdir(screenFolderPath)

        return screenFolderPath

    elif mark == False:
        return screenFolderPath

    else:
        raise ValueError("mark參數應為boolean type")


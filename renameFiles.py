import os
os.chdir('D:\AGS_en_CA_TranslatedReleased')

for f in os.listdir(os.getcwd()):
    f_name, f_ext=os.path.splitext(f)
    f_title, f_GUID, f_num, f_lang, f_non=f_name.split('=')
    new_name= '{}={}={}{}'.format(f_title,f_GUID,f_num, f_ext)
    os.rename(f, new_name)

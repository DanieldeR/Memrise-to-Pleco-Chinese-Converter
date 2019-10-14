import pinyin
import pandas as pd

f_name = str(input("What file would you like to convert:"))

df = pd.read_csv(f_name)

def get_pinyin(x):
    print()

    try:
        return pinyin.get(x.iloc[0], format = 'numerical')
    except:
        return "No pinyin found"


df['pinyin'] = df[['Label']].apply(lambda x: get_pinyin(x), axis = 1)

output_f_name = f_name.split('.')[0] + "_converted.tsv"
df.to_csv(output_f_name, sep='\t', columns = ['Label', 'pinyin'], index =
          False, header = False)

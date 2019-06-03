import numpy as np
import pandas
import many_plots


filepath = '/home/jessedd/data/reprocudibility/'
filename = 'sst5.tsv'

def main():
    df = pandas.read_csv(filepath + filename, sep='\t')
    print_data(df)
    cur_indices = (df['model.encoder.architecture.type'] == 'lstm') & (df['dataset_reader.sample'] == 8543)
    
    dev_accs = df[cur_indices]['best_validation_accuracy'].tolist()


    many_plots.generate(dev_accs)
    
    import pdb; pdb.set_trace()




def print_data(df):
    for key in df.keys():
        vals = df[key].unique()
        if len(vals) < 5:
            print(key, vals)


if __name__ == '__main__':
    main()

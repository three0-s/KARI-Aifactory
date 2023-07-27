import argparse
import pandas as pd
import os.path as osp



def parse_args():
    """Parse parameters."""
    parser = argparse.ArgumentParser(
        description='Make AIFactory submission file')
    parser.add_argument('--txt', help='test output file')
    parser.add_argument('--outdir', help='save path')
    
    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    df = pd.read_table(args.txt, names=['File', 'Confidence', 'X1', 'Y1', 'X2', 'Y2', 'X3', 'Y3', 'X4', 'Y4'], sep=' ')
    df['File'] = [fname[:8] for fname in df['File']]
    print(f"Before: {len(df)}")
    
    df = df.sort_values(by=['File','Confidence'])
    print(f"After: {len(df)}")
    print(df)
    df.to_csv(osp.join(args.outdir, "submission.csv"), index=False)


if __name__ == "__main__":
    main()
    
import pandas as pd

df_xyz = pd.read_csv('DATASETS/CIE_xyz_1931_2deg.csv',names=['x','y','z'],index_col=0)
df_illum = pd.read_csv('DATASETS/CIE_std_illum_D65.csv',names=['s'],index_col=0)
df_xyz = df_xyz.loc[360:780]
df_illum = df_illum.loc[360:780]
(Xw,Yw,Zw) = df_xyz.T.dot(df_illum['s'])
(Xn,Yn,Zn)=(Xw/Yw*100,Yw/Yw*100,Zw/Yw*100)

def spectrum_xyz(spec):
    return df_xyz.mul(df_illum['s'],axis=0).T.dot(spec)/Yw*100

def xyz_lab(X,Y,Z):
    def f(t):
        return t**(1/3) if t > (6/29)**3 else 1/3*(29/6)**2*t+4/29
    fy = f(Y/Yn)
    return 116*fy-16,500*(f(X/Xn)-fy),200*(fy-f(Z/Zn))

# 反射スペクトルから色彩値の計算
色彩値は以下の式で定義される
```math
\begin{aligned}
X &= k \int_{360}^{780}S(\lambda)R(\lambda)x(\lambda)dx \\
Y &= k \int_{360}^{780}S(\lambda)R(\lambda)y(\lambda)dx \\
Z &= k \int_{360}^{780}S(\lambda)R(\lambda)z(\lambda)dx 
\end{aligned}
```
ここで、$`S(\lambda)`$はイルミナントの分光分布の相対強度関数、$`R(\lambda)`$は分光反射率、$`x(\lambda)`$、$`y(\lambda)`$、$`x(\lambda)`$は等色関数の刺激値である。
また$`k`$は透過・反射の場合
````math
k = \frac{100}{\int_{360}^{780}S(\lambda)y(\lambda)dx}
````
実際の計算では離散的なデータのため
```math
\begin{aligned}
X &= \sum_{360}^{780}S(\lambda)R(\lambda)x(\lambda) \\
Y &= \sum_{360}^{780}S(\lambda)R(\lambda)y(\lambda) \\
Z &= \sum_{360}^{780}S(\lambda)R(\lambda)z(\lambda)
\end{aligned}
```
# CIELABの計算
```math
\begin{aligned}
L^* &= 116f(Y/Yn)-16 \\
a^* &= 500[f(X/Xn)-f(Y/Yn)] \\
b^* &= 200[f(Y/Yn)-f(Z/Zn)]
\end{aligned}
```
ここで
```math
f(t)=\begin{cases}
t^{1/3} & t > (6/29)^3 \\
\frac{1}{3}(\frac{29}{6})^2t+\frac{4}{29} & \text{otherwise}
\end{cases}
```
# CIE Lab色空間の表示
## $`L^*a^*b^*`$からXYZへの変換
```math
\begin{aligned}
f_y &= \frac{L^*+16}{116} \\
f_x &= f_{y}+\frac{a^*}{500} \\
f_z &= f_{y}-\frac{b^*}{200}
\end{aligned}
```
とすると
```math
\begin{aligned}
 Y &= \left\{ \begin{array}{ll}
  f_{y}^{3}Y_{n} & (f_{y} > 6/29) \\
  (3/29)^{3} (116f_{y} − 16) Y_{n} & (f_{y} \leq 6/29) 
 \end{array} \right. \\
 X &= \left\{ \begin{array}{ll}
  f_{x}^{3}X_{n} & (f_{x} > 6/29) \\
  (3/29)^{3} (116f_{x} − 16) X_{n} & (f_{x} \leq 6/29)
 \end{array} \right. \\
  Z &= \left\{ \begin{array}{ll}
  f_{z}^{3}Z_{n} & (f_{z} > 6/29) \\
  (3/29)^{3} (116f_{z} − 16) Z_{n} & (f_{z} \leq 6/29)
 \end{array} \right. \\
\end{aligned}
```
## XYZ値からSRGBへ計算する
### XYZ値からリニアRGBを計算する
```math
\begin{aligned}
R &= 3.5064X - 1.7400Y - 0.5441Z  \\
G &= -1.0690X + 1.9777Y + 0.0352Z \\ 
B &= 0.0563X - 0.1970Y + 1.0511Z \\
\end{aligned}
```
### リニアRGBからsRGBへ
モニター画面の輝度の増加がRGB値の増加と直線関係でないためガンマ補正を行う
```math
\begin{aligned}
R'= R^{\frac{1}{2.2}} \\
G'= G^{\frac{1}{2.2}} \\
B'= B^{\frac{1}{2.2}} \\
\end{aligned}
```
# DATASETS
## イルミナント
[A光源](https://cie.co.at/datatable/cie-standard-illuminant-1-nm)
[D50光源](https://cie.co.at/datatable/cie-standard-illuminant-d50)
[D65光源](https://cie.co.at/datatable/cie-standard-illuminant-d65)
## 等色関数
[CIE 1931 2°測色標準観察者](https://cie.co.at/datatable/cie-1931-colour-matching-functions-2-degree-observer)
[CIE 1964 10°測色標準観察者](https://cie.co.at/datatable/cie-1964-colour-matching-functions-10-degree-observer)
# 参考
- [色彩値XYZを計算してみよう](https://www.xrite.com/ja-jp/blog/calculate-color-value-xyz)
- [Lab色空間](https://ja.wikipedia.org/wiki/Lab色空間)
# CIEモジュール
## cie.sperctum_xyz(spec)
スペクトルからX,Y,Zを返す
## cie.xyz_lab(X,Y,Z)
X,Y,Zから$L^*$,$a^*$,$b^*$を返す

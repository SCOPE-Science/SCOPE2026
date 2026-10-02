# Threshold bifurcation for f_t = A_b o S_t: exact neutral fixed point and rigorous upper bound t_c <= (sqrt(3)-1)/(4*pi)

## Context

Let

A_b = [[3,1,0],[1,1,1],[0,1,1]]

act on T^3, and let

S_t(x_1,x_2,x_3) = (x_1+2t sin(2*pi*x_2), x_2+2t sin(2*pi*x_3), x_3) mod 1.

Set f_t=A_b o S_t.  The Anosov-threshold parameter is

t_c = sup{tau in (0,1] : f_s is Anosov for every s in [0,tau)}.

The statement below gives an exact obstruction point and hence a rigorous upper bound on t_c.  It does not identify the exact threshold and does not by itself prove a loss of uniform mixing.

## Result

Let p_2=(1/2,0,1/2) and

t_*=(sqrt(3)-1)/(4*pi).

Then:

1. p_2 is a fixed point of f_t for every t.
2. Writing s=4*pi*t,

   Df_t(p_2)=A_b [[1,s,0],[0,1,-s],[0,0,1]]

   and

   det(Df_t(p_2)-I)=s^2+2s-2.
3. At s_*=sqrt(3)-1 this determinant vanishes transversely, with derivative 2*sqrt(3), and

   spec(Df_{t_*}(p_2))={1, 2+sqrt(5), 2-sqrt(5)}.

   The eigenvalue 1 is simple.
4. Therefore f_{t_*} is not Anosov and

   t_c <= (sqrt(3)-1)/(4*pi) = 0.0582548... .
5. If mu(t) denotes the real multiplier continuing the weak unstable eigenvalue mu(0)=1.688892... to mu(t_*)=1, then

   d mu/dt |_{t=t_*} = -2*pi*sqrt(3).

## Proof

Since sin(0)=sin(pi)=0, S_t(p_2)=p_2.  Moreover A_b p_2=p_2+(1,1,0), so p_2 is fixed on T^3.

At p_2 the two relevant cosine factors are +1 and -1, giving the displayed derivative matrix.  Direct expansion yields

det(Df_t(p_2)-I)=s^2+2s-2,

whose unique nonnegative root is s_*=sqrt(3)-1.  The derivative with respect to s is 2(s+1), hence equals 2*sqrt(3) at the root.

The characteristic polynomial is

-lambda^3 + 5 lambda^2 + (s^2+2s-5) lambda - 1.

At s=s_* one has s^2+2s=2, so this factors as

-(lambda-1)(lambda^2-4lambda-1).

Thus the remaining multipliers are 2+sqrt(5) and 2-sqrt(5), both off the unit circle.  An Anosov diffeomorphism has only hyperbolic periodic points, so the fixed point with multiplier 1 rules out Anosov at t=t_*.  The definition of t_c then gives t_c<=t_*.

For the simple eigenvalue branch, exact left and right eigenvectors at s_* and the standard simple-eigenvalue derivative formula give d mu/ds=-sqrt(3)/2.  Since ds/dt=4*pi, d mu/dt=-2*pi*sqrt(3).

## Reproducibility

Run

`python3 artifacts/bifurc.py`

with SymPy and NumPy.  The script checks the determinant identities, the characteristic polynomial, the fixed point, numerical eigenvalue tracking and the multiplier derivative.

## Limitations

This result proves only the upper bound t_c<=t_* and the explicit neutral-fixed-point mechanism.  It does not prove t_c=t_*, Anosov persistence on all of [0,t_*), or non-uniformity of exponential mixing as t approaches the threshold.

"""Independent recomputation of interval numerical ingredients for the Hopf theorem.
Requires mpmath (tested using mpmath 1.3.0). No external data or network.
All intervals use mpmath's interval arithmetic rather than point sampling.
The analytic root-count and Hopf reduction are proved in RESULT.md.
"""
from mpmath import iv

iv.dps = 50
D = iv.mpf

def Q(t):
    return (15+4*iv.cos(t))*iv.sin(D('1.5')*t) + (5*t-4*iv.sin(t))*iv.cos(D('1.5')*t)

def alpha(t):
    return t*(t-D('.8')*iv.sin(t))/(80*(1-iv.cos(3*t)))

def positive(x):
    return x.a > D('0')

def negative(x):
    return x.b < D('0')

def inside(x,lo,hi):
    return x.a>D(lo) and x.b<D(hi)

assert positive(Q(D('1.84781468')))
assert negative(Q(D('1.84781469')))
assert negative(Q(D('3.49962992')))
assert positive(Q(D('3.49962994')))
x=D(['1.84781468','1.84781469'])
y=D(['3.49962992','3.49962994'])
al=alpha(x)
assert inside(al, '0.09529711', '0.09529713')
assert inside(alpha(y), '0.11199127', '0.11199129')
assert alpha(y).a > al.b
w=x/20
z=iv.mpc(0, 1)*w
E=iv.exp(-60*z)
H=(1-E)/z
Dp=(1-D('.8')*iv.exp(-20*z)
    +al*D('.2')*(60*z*E-(1-E))/(z*z))
root_derivative=-D('.2')*H/Dp
c=(al*D('.008')*H*(iv.re(H)**2+iv.im(H)**2)+D('-.31')**3)/Dp
assert inside(iv.re(root_derivative), '0.04596360', '0.04596366')
assert inside(iv.re(c), '-0.01223645', '-0.01223642')
amplitude=2*iv.sqrt(iv.re(root_derivative)/(-iv.re(c)))
assert inside(amplitude, '3.87622', '3.87624')
# Analytic group eigenvalues (Walsh modes of a three-cube) are checked exactly.
from fractions import Fraction as F
c1,c2,c3=F(15,100),F(5,100),F(1,100)
mu=[3*c1+3*c2+c3,c1-c2-c3,-c1-c2+c3,-3*c1+3*c2-c3]
assert sorted(F(1,2)+v for v in mu)==[F(19,100),F(31,100),F(59,100),F(111,100)]
print('VERIFY_OK root_signs=4 rigorous_interval_comparisons=5 Walsh_eigenvalues=4')
print('alpha_star',al,'second_center',alpha(y))
print('crossing_real',iv.re(root_derivative),'cubic_real',iv.re(c))
print('physical_amplitude_coefficient',amplitude)

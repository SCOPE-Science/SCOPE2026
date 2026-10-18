import sympy as sp

d = sp.symbols("d", integer=True, positive=True)
a = 1/(d+1)
b = d/(d+1)
c = sp.simplify((a+b)/2)

assert sp.simplify(a+b-1) == 0
assert sp.simplify(c-sp.Rational(1,2)) == 0
assert sp.simplify((b-a)/2 - (d-1)/(2*(d+1))) == 0

# Dilation exponent: I_t scales as s^((d-1)(1-t)).
e_num = sp.simplify((d-1)*(1-sp.Rational(1,2)))
e_den = sp.simplify(((d-1)*(1-a) + (d-1)*(1-b))/2)
assert sp.simplify(e_num-e_den) == 0

# Exact midpoint-kernel coefficient from two integrations by parts.
Fa, Fc, Fb, Fpc = sp.symbols("Fa Fc Fb Fpc")
left_piece = (c-a)*Fpc - Fc + Fa
right_piece = -(b-c)*Fpc + Fb - Fc
kernel_integral = sp.simplify(left_piece + right_piece)
assert sp.simplify(kernel_integral - (Fa+Fb-2*Fc)) == 0

# The logarithmic Hellinger deficit is one half of that second difference.
jensen_gap = sp.simplify((Fa+Fb)/2-Fc)
assert sp.simplify(jensen_gap-kernel_integral/2) == 0

print("VERIFY_OK")
print("exponent_sum=1")
print("hellinger_midpoint_exponent=1/2")
print("similarity_scaling_cancels=true")
print("midpoint_variance_kernel_factor=1/2")

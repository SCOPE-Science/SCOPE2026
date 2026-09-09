"""Degree typecheck for lane-447 target claim (integer arithmetic only).

Target (literal): x in (t-s,s)=(83,5); 3*{x} = alpha_1 * y with y in stem 86.
Bracket: <alpha_1, 3, beta_{9/8}> carried in stem 83 at p=3.

Uses only:
  |alpha_1| = 2p-3 = 3 at p=3 (Ravenel Green Book, Greek-letter construction;
    alpha_1 in ANSS E2^{1,4}, stem 3; detects order-3 in pi_3).
  |beta_{i/j}| stem = 2*i*(p^2-1) - 2*j*(p-1) - 2  (Ext^{2, 2i(p^2-1)-2j(p-1)}).
    Check: p=3,i=j=1 -> 16-4-2 = 10 = known |beta_1| stem 10. OK.
  |<a,b,c>| = |a|+|b|+|c|+1 (Toda bracket, when defined; indeterminacy preserves stem).
  |u*v| = |u|+|v|; |3*z| = |z| (3 is degree-0 map).
"""
p = 3
alpha1_stem = 2*p - 3  # 3

def beta_stem(i, j, p=3):
    return 2*i*(p*p-1) - 2*j*(p-1) - 2

b98 = beta_stem(9, 8)  # 2*9*8 - 2*8*2 - 2 = 144-32-2 = 110
bracket_stem = alpha1_stem + 0 + b98 + 1  # 114

x_stem, x_filt = 83, 5
y_stem = 86
lhs_ext = x_stem            # |3*{x}| = 83
rhs_ext = alpha1_stem + y_stem  # 89
gap_ext = rhs_ext - lhs_ext    # 6
gap_bracket = bracket_stem - x_stem  # 31

# Parity: any <alpha1,3,beta_{i/j}> stem is even (3+0+even+1), 83 is odd.
parity_note = (alpha1_stem + 0 + beta_stem(1,1) + 1) % 2  # 0 = even; general since beta even

print(f"alpha1 stem = {alpha1_stem}")
print(f"beta_1 stem check = {beta_stem(1,1)} (expect 10)")
print(f"beta_9/8 stem = {b98}")
print(f"bracket <a1,3,b98> stem = {bracket_stem} (expect 114)")
print(f"target x stem = {x_stem}; gap bracket = {gap_bracket} (expect 31)")
print(f"hidden ext LHS stem = {lhs_ext}, RHS stem = {rhs_ext}, gap = {gap_ext} (expect 6)")
print(f"bracket parity (0=even) = {parity_note}; x parity (83 mod 2) = {x_stem % 2}")
assert beta_stem(1,1) == 10
assert b98 == 110
assert bracket_stem == 114
assert gap_ext == 6
assert gap_bracket == 31
assert lhs_ext != rhs_ext
assert bracket_stem != x_stem
print("VERIFY_OK: literal target ill-typed by gaps 6 (extension) and 31 (bracket); parity even-vs-odd.")

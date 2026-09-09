"""Extended stress battery for lane-447 literal target (integer arithmetic only).

Supplements degree_check.py with:
 (a) exhaustive beta-stem scan for the value needed to land <a1,3,c> at 83,
 (b) hidden-extension repair scan (which y stem would typecheck),
 (c) swapped-variant check preserving all three named objects,
 (d) ANSS d_r stem bookkeeping (d_r drops stem by 1; Moss bracket filtration cap),
 (e) parity lemma orientation checks.
All claims reduce to integer arithmetic + standard E2 addresses:
  Ext^{s,t}(BP_*,BP_*BP) with BP_*,BP_*BP even => Ext^{s,t}=0 for t odd.
  alpha_i in Ext^{1,2(p-1)i}, stem 2(p-1)i-1 (p=3: 4i-1; alpha_1 stem 3).
  beta_{i/j} in Ext^{2,2i(p^2-1)-2j(p-1)}, stem even (p=3: t mult of 4).
  3-fold Toda bracket shift +1; |uv|=|u|+|v|; |3z|=|z|.
"""
p = 3
a1 = 2*(p-1)*1 - 1          # 3
assert a1 == 3
def beta_stem(i, j):
    return 2*i*(p*p-1) - 2*j*(p-1) - 2
def beta_t(i, j):
    return 2*i*(p*p-1) - 2*j*(p-1)

# (a) needed third-entry stem for bracket at 83: 3+0+|c|+1=83 -> |c|=79
need_c = 83 - a1 - 0 - 1
print("needed |c| for bracket at 83:", need_c)
assert need_c == 79
hits = [(i, j) for i in range(1, 60) for j in range(1, 20) if beta_stem(i, j) == need_c]
print("beta hits at stem 79 (i<60,j<20):", hits)
assert hits == []
# orientation: beta t even => stem even; 79 odd => no hits for ANY i,j (proof, not just scan)
print("parity: all beta t even, stems even; 79 odd -> uninhabited at all indices.")

# (b) repair scan for 3*{x83} = a1*y
repairs = [y for y in range(70, 100) if 3 + y == 83]
print("y stems with 3+|y|=83:", repairs)
assert repairs == [80]
print("stated y=86 gives", 3+86, "gap", (3+86)-83)
assert (3+86)-83 == 6

# (c) swapped variant 3*{y86} = a1*{x83}: stems 86 vs 86
print("swapped: LHS 86 vs RHS", 3+83)
assert 3+83 == 86

# (d) ANSS d_r: E_r^{s,t} -> E_r^{s+r,t+r-1}; stem (t-s) drops by exactly 1.
# x at (t-s,s)=(83,5) => t=88. d5 target: s=10,t=92,stem 82. Never stem 86/89.
t_x, s_x = 88, 5
for r in [3, 5, 7, 9]:
    print(f"d{r} on x: -> (stem {t_x-s_x-1}, filt {s_x+r})")
assert t_x - s_x == 83
# Moss: E2 bracket filt <= 1+0+2 = 3 < claimed carrier filt 5
print("Moss cap filt<=3 vs claimed filt 5: needs unlogged crossing jump.")
assert 1+0+2 < 5

# (e) named instance + parity samples
print("named <a1,3,b9/8> stem:", a1+0+beta_stem(9,8)+1)
assert a1+0+beta_stem(9,8)+1 == 114
assert (a1+0+beta_stem(1,1)+1) % 2 == 0  # even
assert 83 % 2 == 1                        # odd
print("VERIFY_OK: extended battery confirms gaps 6/31, parity even-vs-odd, repairs {80, swapped}.")

"""Verify the HAW -> Schmidt(1/12, 1/2) transfer constants explicitly.
HAW game (BNY/McMullen convention): Bob ball radius R; Alice deletes H^{(eps)},
eps <= beta'*R; Bob replies radius >= beta'*R disjoint from deletion.
Schmidt game: Bob ball R; Alice sub-ball alpha*R; Bob sub-sub-ball beta*alpha*R.
Claim: HAW at beta'=1/24 implies Schmidt (alpha,beta)=(1/12,1/2)-winning.
Check each inequality with exact rationals."""
from fractions import Fraction as Q
alpha = Q(1,12); beta = Q(1,2); bp = Q(1,24)
R = Q(1,1)  # scale-free; all homogeneous
# 1. Alice avoidance: move center by (1-alpha)R away from H.
move = (1-alpha)*R
dist_after = move  # worst case dist(c,H)=0, moving away
need_clear = bp*R + alpha*R  # eps_max + Alice radius
print("dist after move:", dist_after, " need >=", need_clear, " OK:", dist_after >= need_clear)
# containment: move + alpha*R <= R ?
print("containment:", move + alpha*R <= R, move + alpha*R, "vs", R)
# 2. Bob reply radius beta*alpha*R >= bp*R ?
print("Bob radius ok:", beta*alpha*R >= bp*R, beta*alpha*R, "vs", bp*R)
# 3. induction: all rounds scale by (beta*alpha)=bp per round; HAW needs >= bp*R_n each round: equality holds.
print("round factor:", beta*alpha, "== bp:", beta*alpha == bp)
# 4. generality: for any alpha0<1/2, any beta0, exists bp>0 with (1-2a)R>eps and beta0*a>=bp
for a_num,a_den in [(1,12),(1,3),(1,100),(49,100)]:
    a = Q(a_num,a_den)
    import math
    assert a < Q(1,2), a
    # need bp <= min(beta0*a, (1-2a)/2 ) for any beta0; take beta0=1/2
    cap = min(Q(1,2)*a, (1-2*a)/2)
    print(f"alpha={a}: feasible bp cap = {cap} (>0: {cap>0})")
print("TRANSFER VERIFIED")

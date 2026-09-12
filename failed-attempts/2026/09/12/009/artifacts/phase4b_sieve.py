"""Phase 4b: TRUE Smart sieve semantics — compatible SYSTEMS (not pairs).
Sage: compatible_systems: CRT-combines per-prime data; the sieve works on the X-SIDE
only (x exponents A, t+1=6 gens), with complement dictionaries for y. Count systems for
x-exponents mod L: per prime q: #valid X-residues ~ q (X in H with 1-X in H ~ q-2+q... ).
For x-side alone: total A mod (q-1): (q-1)^6; valid: those with X in H, 1-X in H:
count = valid_X * ker where valid_X = #{X in H : 1-X in H} ~ q, ker=(q-1)^6/|H| ~ (q-1)^5.
So per-prime survivors ~ q*(q-1)^5 vs (q-1)^6 total: fraction ~ q/(q-1) ~ 1?! NO sieve power
on x-side alone per prime?? The power comes from COMBINING primes via CRT: L=lcm, and
FINAL lift uniqueness needs L>2B. #final systems ~ L^6 * prod(frac)... frac~1 each?!
Hmm, that says sieve does nothing?? Wrong: per-prime constraint is X mod q in GoodSet
(size ~q out of q possibilities — trivially true since X in H subset F_q, and GoodSet
~ all of H...). Wait GoodSet = {X in F_q^*: X,1-X both S3-smooth-ish (in H)}. For random
X in F_q^*: P(X in H)=|H|/(q-1)~1, P(1-X in H)~1. So indeed for Q with rho generating
everything, ONE prime gives NO cut. The sieve works because... hmm, actually NO: the
sieve in Smart works on the COMBINED (A,B) data? Let me look at Sage construct_complement
+ compatible_systems + solutions_from_systems to get the true combinatorics. Key question:
is the sieve even effective for K=Q rank-5 S-unit equations with B~2400? Evidence: Sage
routinely solves rank-5 S-unit equations (de Weger: S with 5 primes takes minutes). The
trick: use MANY primes; combined moduli L huge; #systems grows like L^5?? and each system
lifts to a tiny box... The total work ~ #systems at final L. If #systems ~ L^5 * c with
L~4800: 2.5e18 — infeasible?! But Sage does it — because Sage ENUMERATES solutions_from_systems
by lifting each CRT system to the box: #lifts per system = (2B/L)^6-ish... total = #systems*(2B/L)^6.
If #systems ~ L^6 * rho_frac with rho_frac = fraction surviving all sieves ~ prod_q (valid_q/q^6?)...
I need the REAL per-prime survival fraction. Let me read Sage's construct_complement_dictionaries
and compatible_systems + solutions_from_systems code carefully instead of guessing.
"""
print("reading sage sieve code...")

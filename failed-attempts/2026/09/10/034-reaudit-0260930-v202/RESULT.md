# The stated quaternion symbol is not in Br(X*) for X*: x0^4+2x1^4-5x2^4-10x3^4=0

## Context

The admitted target claimed the diagonal-quartic K3 surface
X*: x0^4+2x1^4-5x2^4-10x3^4=0 over Q is everywhere locally soluble and
that A=((x0^2+2x1^2)/x2^2,-10) in Br(X*)[2] is transcendental with total
local-invariant sum 1/2, hence a transcendental Brauer-Manin obstruction
to the Hasse principle. General-member vanishing (Bright 2011), odd-order
results (Ieronymou-Skorobogatov 2015; Ieronymou 2023), a 3-torsion example
(Preu 2013), and counting results (Santens 2023) leave this named member
and symbol undecided. The result below decides the exact target
conjunction by rigorous disproof of its first clause.

## Definitions

- X* subset P^3_Q: x0^4+2x1^4-5x2^4-10x3^4=0.
- k(X*): function field.
- f=(x0^2+2x1^2)/x2^2 in k(X*)^times, b=-10 in Q^times.
- (f,b) in Br(k(X*))[2]: quaternion class.
- Br(X*): unramified subgroup of Br(k(X*)) (purity, X* smooth).
- K=Q(sqrt(-2)), alpha^2=-2, h=x0^2+2x1^2=(x0-alpha x1)(x0+alpha x1)=h_+ h_-.
- D_+=V(x0-alpha x1) cap X*_K.
- Residue for quaternion (f,g) at prime divisor D, char != 2:
  d_D((f,g))=(-1)^{v_D(f)v_D(g)} overline{f^{v_D(g)}/g^{v_D(f)}}
  in k(D)^times/2. For constant g=b: d_D((f,b))=overline{b^{v_D(f)}}.

## Result

Let X* and (f,b) be as above. Then (f,b)_Q is ramified along a prime
divisor after base change to K=Q(sqrt(-2)), hence
(f,b)_Q not in Br(X*_Q).

In particular the target conjunction — A in Br(X*)[2], transcendental,
total invariant sum 1/2 — is false as stated, since the first clause
fails. No assertion is made about X*(Q), local solubility, or any
repaired symbol.

## Proof / Evidence

1. Smoothness and function field: partials of F are
   (4x0^3,8x1^3,-20x2^3,-40x3^3), vanishing jointly in P^3 only at
   (0,0,0,0). Hence X* smooth quartic (K3); smooth hypersurface in P^3
   integral (if F=GH then V(G) cap V(H) != empty and grad F vanishes
   there). f nonzero: at Qbar-point x0=1,x1=x3=0,x2^4=1/5 on X*,
   f=1.
2. Divisor: over K, H cap X*_K=D_+ union D_- with
   D_pm=V(x0 mp alpha x1) cap X*_K. D_+ is an irreducible prime divisor,
   isomorphic over K to smooth plane quartic
   C0: 6y1^4-5y2^4-10y3^4=0 via [x0:x1:x2:x3]->[x1:x2:x3], inverse
   [y1:y2:y3]->[alpha y1:y1:y2:y3] (since alpha^4=4, F restricts to
   6x1^4-5x2^4-10x3^4). C0 smooth (all coeffs nonzero); smooth plane
   curve geometrically irreducible (reducible implies components meet by
   Bezout and intersection is singular).
3. Valuation: Qbar-point p: x1=1,x0=alpha,x3=0,x2=t with 5t^4=6 satisfies
   s^2+2=0, s^4+2-5t^4=4+2-6=0, t,s != 0. In chart x1=1,
   X*_K: u0^4+2-5u2^4-10u3^4=0, H_+: u0-alpha=0, gradients
   (4alpha^3,-20t^3,0) vs (1,0,0) independent since t != 0. Hence
   transverse smooth meeting; h_+ regular parameter, (h_+) height-1
   prime of O_{X*_K,p}, v_{D_+}(h_+)=1; h_-=2alpha != 0 and x2=t != 0
   units, so v_{D_+}(f)=1+0-0=1 (odd).
4. Residue: d_{D_+}((f,b))=[b]=[-10] in K(D_+)^times/2. Since
   (x0/x1)^2=-2 in K(D_+), [-2]=0 and [-10]=[5]. Lemma: 5 not in K^times2:
   (a+b sqrt(-2))^2=5 gives a^2-2b^2=5, 2ab=0; a=0 gives -2b^2=5
   impossible over Q (LHS<=0<5); b=0 gives a^2=5 impossible (sqrt5 not in
   Q via 5|p^2=>5|p mod-5 check + descent). Lift: D_+ cong C0 smooth
   projective geometrically integral => constant field K, H^0=K*; if
   5=u^2 in K(C0) then 2 div(u)=0 => div(u)=0 => u in K^times,
   contradiction. Hence residue nonzero; (f,b)_K ramified, not in
   Br(X*_K).
5. Descent: pi:X*_K->X*_Q pullback Br(X*_Q)->Br(X*_K) sends (f,b)_Q to
   (f,b)_K. Unramified over Q would pull back unramified; ramification
   along D_+ gives (f,b)_Q not in Br(X*_Q).

Computation is exact stdlib-only (integer identities s^4=4, 5t^4=6,
mod-5 squares); no floating point, no Sage dependency.

## Limitations

Refutes only the Azumaya clause of the target as stated. Does not decide
local solubility of X*, X*(Q), nor whether a repaired same-scope symbol
could obstruct the Hasse principle.

## Reproducibility

- `python3 output/artifacts/verify.py` prints `VERIFY_OK`.
- Checks: X*/C0 smoothness (monomial partials), transverse point
  identities, 5 not square in Q(sqrt(-2)) via mod-5 + sign argument,
  residue logic.
- References for residue formula: Gille-Szamuely, Central Simple Algebras
  and Galois Cohomology, Thm 6.8.3-6.8.4.

## References

- M. Bright, Brauer groups of diagonal quartic surfaces, J. Symbolic
  Comput. 2006. https://doi.org/10.1016/j.jsc.2005.10.001
- M. Bright, The Brauer-Manin obstruction on a general diagonal quartic
  surface, Acta Arith. 147, 2011. https://doi.org/10.4064/aa147-3-8
- E. Ieronymou, Diagonal quartic surfaces and transcendental elements of
  the Brauer group, JIMJ 2010. https://doi.org/10.1017/s1474748010000149
- E. Ieronymou, A. Skorobogatov, Odd order Brauer-Manin obstruction on
  diagonal quartic surfaces, Adv. Math. 270, 2015.
  https://doi.org/10.1016/j.aim.2014.11.004
- E. Ieronymou, Odd torsion Brauer elements and arithmetic of diagonal
  quartic surfaces, Trans. AMS 2023; arXiv:2209.15388v3.
  https://arxiv.org/html/2209.15388v3
- T. Preu, Example of a transcendental 3-torsion Brauer-Manin obstruction
  on a diagonal quartic surface, 2013.
  https://doi.org/10.1017/cbo9781139525350.013
- T. Santens, Diagonal quartic surfaces with a Brauer-Manin obstruction,
  Compositio 2023; arXiv:2201.04573. https://arxiv.org/abs/2201.04573

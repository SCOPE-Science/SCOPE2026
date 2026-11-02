---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-26.md",
      "INDEPENDENT_AUDIT_2026-10-26.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Reconstructed the frozen RESULT.md statement for every integer N>=2,m>=3, nondegenerate real equality case A,B,C>0, with smooth v=Delta^(floor(m/2)-1)u in the stated graph-norm closure; the conclusion concerns P_(m-2)u only. With s=sqrt(N^2+4(m-2)(N-1)), the source square coefficients obey c_e^2-N*c_e=(m-2)(N-1), c_o^2+(N-2)*c_o=(m-1)(N-1), 2*c_e-N+2=N+2*c_o=s+2. Even order: A+b^2 B-b(s+2)C = ||Delta v+b x.grad v+b c_e v||_2^2 + b^2 integral(|x|^2|grad v|^2-(x.grad v)^2); equality with b=sqrt(A/B) forces the square and angular defect to vanish, hence smooth radial v. Odd order: A+b^2 B-b(s+2)C=||grad Delta v+b x Delta v+b c_o grad v||_2^2, forcing the vector equation. Set w=Delta v+b c_o v; grad w=-b x Delta v makes w radial, then Delta v and (since c_o>0) v radial. Even radial ODE v"+((N-1)/r+b*r)v"prime+b*c_e*v=0; odd write y=v"prime/r, obtaining y"+((N+1)/r+b*r)y"prime+b(N+c_o)y=0. Smooth radial initial-value uniqueness at r=0 makes each regular solution space one-dimensional; Kummer functions give exactly the two claimed hypergeometric P_(m-2) profiles with parameters (N-s)/4 and (N+2-s)/4. Independently rederived the full weighted-tensor Fourier energy identity and checked the c_e,c_o and hypergeometric parameter algebra exactly with SymPy, plus four independent ODE residual samples (N,m)=(2,3),(3,4),(4,5),(5,8), numerically negligible, not a substitute for the all-parameter proof. The graph-domain hypothesis justifies source cutoff extension; no claim of classification for arbitrary abstract seminorm-completion elements or u modulo nullspace is made.

## originality

FAIL

Decisive stronger prior mathematical coverage: the claimed entire regular equality-profile classification is a specific Fourier plus inverse-square ground-state reparametrization of the known complete optimizer classification for sharp L2 Caffarelli-Kohn-Nirenberg inequalities, especially Cazacu-Flynn-Lam (2021) Theorem 1.1/Remark 2.2 and the general Theorem A as stated in Do-Lam-Lu-Nguyen (2026). Let k=m-1, f=Fourier(u), and g(xi)=|xi|^k f(xi). The full tensor Frobenius norm and Plancherel give A=int |xi|^2|g|^2, C=int |g|^2, and B=int(|grad g|^2+k(N-1)|xi|^{-2}|g|^2). Set gamma=(2-N+sqrt(N^2+4(m-2)(N-1)))/2>0, so gamma(gamma+N-2)=k(N-1). The standard inverse-square ground-state transform h=|xi|^{-gamma}g and integration by parts yield B=int |xi|^{2gamma}|grad h|^2, A=int |xi|^{2gamma+2}|h|^2, C=int |xi|^{2gamma}|h|^2, initially on the smooth punctured core and then in the square/weighted completion by density. These are exactly the L2 Caffarelli-Kohn-Nirenberg functionals with (a,b)=(-gamma-1,-gamma). The pair lies in the original 2021 A1 region because b+1-a=2>0 and b=-gamma<=(N-2)/2 for N>=2. Cazacu-Flynn-Lam Theorem 1.1 (and 2026 Do-Lam-Lu-Nguyen Theorem A) gives the sharp constant (N-(a+b+1))/2=(N+2gamma)/2=(2+sqrt(N^2+4(m-2)(N-1)))/2 and ALL equality profiles h=D exp(-lambda|xi|^2/2), D nonzero, lambda>0. Thus g=D|xi|^gamma exp(-lambda|xi|^2/2) is necessarily radial and unique up to complex/real scalar and dilation. Hu-Liu-Zou already give the inverse-Fourier Kummer profiles; Kummer transformation matches even (1-gamma)/2=(N-s)/4 and odd (2-gamma)/2=(N+2-s)/4, with spatial b=1/lambda. Therefore both existence AND exhaustion of the assigned profiles are implied by published general weighted CKN optimizer classification, even though the focal paper states only existence.

## value

FAIL

The equality manifold of a sharp genuinely higher-order Heisenberg inequality is a natural mathematically motivated object; ruling out nonradial equality profiles would be structurally useful if unknown. Here the actual asserted set is fully determined by the existing 2009/2021 free-parameter weighted CKN optimizer classification after a direct Fourier/tensor norm calculation and inverse-square ground-state substitution, while the precise spatial hypergeometric profiles were already constructed in the focal 2026 source. The proposed work neither identifies a new independent invariant nor proves stability, an unaddressed parameter regime, a new spectral estimate, or a classification outside the known CKN optimizer family. Thus the claimed contribution is a mechanically implied special case of a stronger existing theorem; this value judgment is separate from correctness and not based on paper size or inaccessible literature.

The dated certificate retains the supplied scientific assessment, sources and limitations.

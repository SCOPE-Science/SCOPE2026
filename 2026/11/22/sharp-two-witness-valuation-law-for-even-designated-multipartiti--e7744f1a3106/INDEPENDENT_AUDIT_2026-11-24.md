# Independent mathematical audit

## correctness

PASS

The marked-part factor 1+Σ_{m≥1}m x^m gives the eta quotient. The critical odd two-dissection can be reconstructed independently: put θ₃(q)=Σ_{a∈ℤ}q^{a²}, θ₄(q)=Σ_{a∈ℤ}(−1)^a q^{a²}, ψ(q)=Σ_{j≥0}q^{j(j+1)/2}. Jacobi products give θ₄(q)=f₁²/f₂, θ₃(q)θ₄(q)=θ₄(q²)², and ψ(q)=f₂²/f₁. Thus F² equals f₄²f₁₂²/(f₂⁷f₆³) times θ₃(q)θ₃(q³), with the prefactor even in q. The odd part of the theta product is the sum over pairs (a,b) of opposite parity. The change (u,v)=(a+3b,a−b) is a bijection onto odd pairs congruent modulo 4 with exponent (u²+3v²)/4. Flipping v exchanges the congruent and noncongruent pairs at the same exponent, so the odd part is 2qψ(q²)ψ(q⁶). Multiplying gives exactly 2qW(q²) as in the frozen proof. The elementary binomial reduction f₁⁸≡f₂⁴ mod 4 and f₃⁴≡f₆² mod 4 makes W even in its argument mod 4, so A₂(4n+3) is 8-divisible. For general H, H(q)²−H(q²) is 2-divisible; each squaring increases the modulus by at least one power of two. Iteration yields the two stated lifts. Powers of F⁴ (resp. F⁸) inherit divisibility by 4 (resp. 8) on odd exponents and by 2 (resp. 4) on exponents 2 mod 4. Convolving with F² against the residue classes proves the required progression-wide lower bounds. At degree three direct extraction gives k(k+1)(k+14)/6 and the stated exact valuations outside k≡2 mod 16. Independent truncation gave F² coefficients (1,2,7,16,39,80,171,328) and F¹⁶=(1,0,8,0,4,0,8,0) mod (16,q⁸). The nonconstant truncation of F¹⁶ squares to zero in that quotient and its contribution to [q⁷]F²(F¹⁶)^m vanishes modulo 16 for every m. Thus A_{16m+2}(7)≡8 mod 16 exactly. Together with divisibility, the two fixed-degree witnesses prove the exact ν₂ of the positive infinite gcd. No frozen checker was executed.

## originality

PASS

Credit the known marked-part series and cited dissection, previous divisibility and the sharp k≡6 mod 8 class as prior, and the prediction as a published conjecture, not a new conjecture. The supported distinct contribution is the proof of exactness uniformly for the remaining even classes, with a uniform low-degree witness in the exceptional residue class, hence a two-coefficient determination. The most related separately indexed result is the odd-parameter branch, not a covering theorem for even k.

## value

PASS

The invariant is motivated by a specific published progression conjecture for a standard partition-generating function. A constructive sharpness theorem for every even tuple order replaces finite evidence with an exact minimum; in the exceptional class where the first coefficient overstates the divisibility, a universally valid second witness makes this precise. The first two coefficients thus determine an invariant of an infinite progression, not just a test sample.

The dated certificate retains the supplied scientific assessment, sources and limitations.

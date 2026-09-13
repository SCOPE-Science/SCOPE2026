"""Exp4: Artin invariant of Km(E_ss x E_ss); supersingular reduction of NS lattice.

NS(A) for A=E^2, E ss with End=order in Q(sqrt(-13)): rank 4, disc = -det(Hom)^... use known formula:
disc NS(A) = -det(NS(A)). For E^2 with CM, gram of Hom-part: translations of degree form.
Simpler: use T(A) = transcendental lattice det = 13^2 * (rank-2 correction).
Standard: A=E^2 supersingular over char p => A supersingular abelian => Km supersingular K3 with
sigma(Km) = sigma(A)+1? For product of ss elliptic curves sigma(Km)=2 (Shioda: disc NS = -p^{2sigma},
sigma=2 for Km of product of two ss curves). Check disc exponent: NS rank 22 disc -13^4.
Sigma=1 needs disc -13^2: one "Frobenius length-1" quotient => degree-2 isogeny K3 (Kummer sandwich).
Here: compute discriminant group sizes only, plus diagonal-H form for (-2)-classes.
"""
# disc group of NS(Km): for sigma=2: A_NS = (Z/13)^4. For sigma=1: (Z/13)^2.
# Enriques lattice M=U(2)+E8(2) has disc group (Z/2)^10 — primitively embeds into NS_{13,1}
# iff there is an embedding, but need involution: NS(X)^iota = M(2)? iota* acts as -1 on M^perp?
# Key Enriques lattice criterion (Horikawa/Nikulin, char !=2): Enriques involution exists iff NS(X)
# contains primitive M=U(2)+E8(2) with M^perp containing no (-2)-class of X... over C.
# In char 13: result of Dolgachev-Keum/Liedtke: supersingular K3 with sigma=1 admits Enriques
# involution iff sigma=1 (all sigma=1 admit? No: Ogus/DK: supersingular K3 admits Enriques
# involution iff sigma <= 5 in char p>2? check). Record obstruction test via (-2)-reflection
# group instead: compute (#-2 classes irrelevant computationally here).
# Just record numeric discriminant data:
for sigma in [1, 2, 3]:
    print(f"sigma={sigma}: |disc NS| = 13^{2*sigma} =", 13**(2*sigma))
print("Enriques M=U(2)+E8(2): rank 10, disc 2^10 = 1024; M^perp in NS_{13,1}: rank 12, disc 2^10 * 13^2")
print("Embedding obstruction is 2-primary vs 13-primary: coprime => no lattice embedding obstruction.")

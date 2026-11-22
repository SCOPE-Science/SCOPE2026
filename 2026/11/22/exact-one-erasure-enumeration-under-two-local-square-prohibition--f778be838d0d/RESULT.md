# Exact one-erasure enumeration under two local square prohibitions

## Finding
Let \(H_n\) count the length-\(n\) binary partial words with exactly one undefined symbol \(\diamond\) that avoid every *compatible* tandem square of half-length two or three. Then, for every \(n\ge0\),
\[
\sum_{n\ge0}H_nz^n=\frac{N(z)}{D(z)^2},\qquad D(z)=1-z^2-z^3-z^4+z^6,
\]
where
\[
\begin{aligned}
N(z)={}&z+4z^2+10z^3+6z^4-z^5-18z^6-29z^7-14z^8\\
&+7z^9+14z^{10}+16z^{11}-4z^{12}-7z^{13}\\
&+2z^{15}+4z^{16}+2z^{17}-4z^{18}.
\end{aligned}
\]
Moreover, with \(\rho=0.713639173536901\ldots\), the smallest-modulus root of \(D\),
\[
H_n\sim c n\rho^{-n},\qquad c=\frac{N(\rho)}{\rho^2D'(\rho)^2}=0.501969614577446\ldots.
\]
The exponential growth base is \(1/\rho=1.401268367939854\ldots\).

## Assumptions and scope
The positions are indexed and the words are **linear**, not circular. The alphabet is \(\{0,1,\diamond\}\). Exactly one position is a hole, and every other position is one of the two defined letters. Two equal-length blocks are *compatible* if they have no disagreeing pair of defined letters in corresponding positions. A square of half-length \(p\) is a factor of length \(2p\) whose halves are compatible. Avoidance is imposed only for \(p\in\{2,3\}\); half-length one is allowed. The empty word has no admissible one-hole realization, so \(H_0=0\). The count retains the hole position and distinguishes binary complementation.

## Proof
A left-to-right deterministic transfer keeps the last five characters (or the shorter prefix before position five), and a bit recording whether the hole has already occurred. From each state append \(0\) or \(1\), or \(\diamond\) only if no hole has been used; disallow the transition if the new last four or six characters split into compatible equal-length halves. Because forbidden factors have length at most six, this is an exact bijection between admissible words and transfer paths.

For all prefixes of length at least five, binary complementation commutes with these transitions. Quotient each pair of complementary five-suffix states and retain the used-hole bit. There are \(16\) orbits with no hole yet; \(40\) with a hole within the last five characters; and \(16\) with the hole already outside this five-character suffix. This gives a \(72\)-state integer-weighted transfer. The middle block is transient: after five binary letters, the hole must leave the suffix. The first and last diagonal blocks are the same \(16\)-state binary transition matrix \(Q\). Therefore its generating-function denominator divides \(\det(I-zQ)^2\).

Newton's exact integer identities applied to \(Q\) give its characteristic polynomial
\[
\chi_Q(t)=t^{10}(t^6-t^4-t^3-t^2+1),
\]
so \(\det(I-zQ)=D(z)\). Thus \(D(z)^2\sum H_nz^n\) is a polynomial. A useful *rigorous degree bound* is \(41\): the five-character initialization costs degree five; each of at most two binary-block resolvents contributes an adjugate of degree at most \(15\); entering and exiting the transient block cost one degree each; and the transient block permits at most four interior steps. The other possible paths have smaller degree. The length-zero-through-four initialization yields a polynomial of degree at most four, and multiplying it by \(D(z)^2\) gives degree at most sixteen. Therefore the complete numerator has degree at most \(41\).

The exact transfer recurrence gives the first \(43\) coefficients \(H_0,\ldots,H_{42}\). Multiplying this finite coefficient vector by the explicit degree-twelve polynomial \(D(z)^2\) yields exactly the displayed \(N(z)\), with zero coefficients at degrees \(19,\ldots,42\). Because the full numerator has degree at most \(41\), this establishes the identity for **every** length, not only the checked lengths.

For the asymptotic, the recurrent part of \(Q\) is one strongly connected, aperiodic eight-vertex component (its directed cycles include lengths two and three); every other component is acyclic. Perron–Frobenius therefore gives a unique dominant positive eigenvalue \(\rho^{-1}\), and all other roots relevant to the numerator have strictly smaller exponential modulus. The computed numerator satisfies \(N(\rho)>0\), so its double pole at \(\rho\) does not cancel. The coefficient of \((1-z/\rho)^{-2}\) is \(N(\rho)/(\rho^2D'(\rho)^2)\); coefficient extraction proves the stated asymptotic.

## Verification
Run `python3 verify_transfer.py` (Python 3 standard library). It independently generates the complete \(72\)-state quotient, computes the exact \(16\)-state characteristic polynomial by Newton identities, verifies the five-step nilpotence, and checks the finite numerator certificate to degree \(42\). It prints `PASS` on success. Run `python3 verify_direct.py`, which independently enumerates literal partial words at all lengths up to twelve and tests each possible forbidden square. Both scripts were executed successfully. The first values are
\[
(H_0,\ldots,H_{20})=(0,1,4,12,16,32,40,66,100,152,224,336,500,742,1092,1612,2372,3476,5088,7436,10852).
\]
The programs are finite **certificates for an algebraic all-length proof**: the degree bound and block characteristic-polynomial argument, rather than unbounded extrapolation from the data, justify the identity.

## Relationship to prior work
Blanchet-Sadri and Mercaş (2009) define compatible squares in partial words and bound the number of distinct squares occurring in a given word. Halava, Harju and Kärki (2010) sharpen such bounds and discuss square occurrences, not this exact restricted avoidance-language enumerator. Both papers were inspected in primary full text, including their main statements and conclusions. A related binary *no-hole circular* enumeration with the same two prohibited half-lengths has a factor \(D(z)\) in its zeta denominator; it does not give the one-hole **linear** count, its numerator, or the double-pole asymptotic. The use of finite transfer matrices is standard; the evaluated one-erasure numerator and resulting prefactor are the specific assertion here.

## Limitations
The theorem does not forbid all squares, does not study more than one hole, and makes no assertion about cyclic or necklace enumeration. Asymptotic decimals are rounded; the exact algebraic expressions define the result. No independent external mathematical validation has been performed. Although specific indexed overlap searches found no equivalent one-hole count, unavailable or unindexed historical enumerations remain a possible originality risk.

## References
1. F. Blanchet-Sadri and R. Mercaş, *A note on the number of squares in a partial word with one hole*, RAIRO Theor. Informatics Appl. **43** (2009), 767–774, https://doi.org/10.1051/ita/2009019 (first day-verified online publication: 2009-10-01).
2. V. Halava, T. Harju and T. Kärki, *On the number of squares in partial words*, RAIRO Theor. Informatics Appl. **44** (2010), 125–138, https://doi.org/10.1051/ita/2010008.

# Five-symbol ambiguity certificates for three-word codes of lengths two, two and three

## Finding
Let \(\Sigma\) be an alphabet of size \(q\ge2\). Choose an unordered pair of distinct length-two words \(X=\{x,y\}\subset\Sigma^2\) and a length-three word \(z\in\Sigma^3\). Regard \(C=X\cup\{z\}\) as a three-word variable-length code. The following conditions are equivalent:

1. \(C\) is not uniquely decipherable: two distinct finite sequences of its codewords have identical concatenation.
2. At least one of the following disjoint possibilities occurs:
   - **Constant long word:** \(z=aaa\) for some \(a\in\Sigma\), with \(aa\in X\).
   - **Alternating long word:** \(z=aba\) with \(a\ne b\) and \(X=\{ab,ba\}\).
3. Some length-five word has two distinct factorizations into members of \(C\).

Consequently the number of non-uniquely-decipherable *unordered, labeled* codebooks of this profile is
\[
B_q=q(q^2-1)+q(q-1)=q(q-1)(q+2).
\]
The total number of these codebooks is \(T_q=\binom{q^2}{2}q^3\). Hence their uniquely decipherable count is \(T_q-B_q\) and the nondecipherability probability under uniform sampling of the codebook is \(2(q+2)/(q^4(q+1))\), asymptotic to \(2/q^4\).

## Assumptions and scope
Codewords are ordinary finite strings over a named alphabet, concatenation is the free-monoid operation, and the two length-two words are required to differ. Swapping these two words does not define another codebook. The length-three codeword is necessarily different from either. The statement is for every integer \(q\ge2\), without a fixed binary-alphabet assumption. It does not assert the analogous classification for longer third codewords, for other length profiles, or for multiset decipherability.

## Proof
**Sufficiency and the length-five bound.** In the constant case, the distinct factorizations \((aaa)(aa)=(aa)(aaa)\) witness ambiguity. In the alternating case, \((aba)(ba)=(ab)(aba)\) witnesses ambiguity. Every two distinct factorizations of a word using only codewords of lengths two and three must have length at least five: at length at most four, the only possible factorizations have length patterns \((2)\), \((3)\), or \((2,2)\), and two-letter fixed-block parsing is unique. Thus these certificates are shortest possible.

**Necessity by an exact finite equality-pattern proof.** Here is an exhaustive symbolic certificate, not a bounded experiment on alphabet size. For an ordered triple \((x,y,z)\), write the seven letter positions of the concatenation \(xyz\) as \((s_1,\dots,s_7)\). A *restricted-growth string* is a sequence \(r_1,\dots,r_7\) with \(r_1=0\) and \(0\le r_i\le1+\max(r_1,\dots,r_{i-1})\). Every partition of the seven positions into equal-symbol classes has exactly one such representation, obtained by numbering classes in first-appearance order. There are exactly \(877\) seven-position partitions; after excluding the \(52\) assignments where the first two two-letter words coincide, \(825\) legitimate symbolic profiles remain. This covers arbitrarily large alphabets because none of the relevant equality questions can distinguish two assignments with the same position partition.

For each symbolic profile, run the classical Sardinas–Patterson residual test. Its first residual set consists of all nonempty suffixes left after removing one distinct codeword from the start of another. Subsequently, for every pending residual \(s\) and every codeword \(c\), remove \(s\) from the front of \(c\) when it is a prefix, and remove \(c\) from the front of \(s\) when it is a prefix. The code is not uniquely decipherable exactly when a residual becomes empty or equals a full codeword. The residual graph is finite: every generated residual is a suffix of a codeword, and a previously visited residual needs no re-expansion. The usual cancellation of a pair of different parsings proves both directions of the test; a successful residual path reconstructs two parsings, while cancellation of the first unequal codewords of any ambiguous message creates the initial residual and then follows these edges.

The supplied standalone `verify.py` enumerates all restricted-growth strings recursively, implements prefix cancellation directly on tuples, and asserts the test agrees on every legitimate symbolic profile with the two explicit structural cases above. It reports that exactly \(10\) eligible symbolic profiles are nondecipherable: \(8\) use exactly two symbols and \(2\) use exactly three. The remaining \(815\) are decipherable. This is a finite exhaustive proof of the necessity condition for all finite alphabets, not an inference from a handful of finite-alphabet trials.

**Counting.** In the constant case, choose \(a\) in \(q\) ways and choose the other short word freely except for \(aa\), in \(q^2-1\) ways. In the alternating case, choose the ordered pair \((a,b)\) of different letters in \(q(q-1)\) ways; the two short words are then forced as an unordered set. The cases are disjoint, giving the displayed formula. The probability formula follows by division by the total \(\binom{q^2}{2}q^3\).

## Verification
The exact symbolic procedure is a terminating equality-pattern enumeration: \(877\) partitions, \(825\) valid triples, and precisely \(10\) nondecipherable patterns. The standalone checker also independently enumerates all literal codebooks for \(q=2,3,4,5\), recovering respectively \(8,30,72,140\) ambiguous codebooks, and verifies the concrete length-five witnesses. Run `python verify.py` using Python's standard library. The finite alphabet sweeps are consistency checks only; the all-\(q\) conclusion follows from complete equality-type coverage.

## Relationship to prior work
Sardinas and Patterson introduced the decidability criterion for unique decipherability in 1953. Blanchet-Sadri's 2001 work analyzed unique, multiset and set decipherability for three-word codes when the first two codewords have equal length. Blanchet-Sadri and Howell's 2002 study pursued the weaker-decipherability equivalence problem for other three-word families. These establish a general decision framework and structural context, not the precise two-pattern failure classification, all-alphabet polynomial, or universal five-symbol shortest-witness statement isolated here. Unlike equal-length comma-free codes or Kraft-equality codebook enumerations, the target is a three-word variable-length uniquely decipherable code and the failure of unique parsing.

## Limitations
The necessity argument is a transparent, fully enumerable symbolic computational certificate rather than a short case-free handwritten classification; independent mathematical checking has not been performed. The uniqueness and shortest-witness conclusions apply only to the stated \((2,2,3)\) length profile. Broader earlier literature on short codebooks may contain equivalent statements that are not indexed or explicitly titled as such. The exact first day of public release of some earlier 2001 material is not independently established here; the precisely dated 2002 public article is used as a conservative dated source anchor, without implying it is the historically first treatment of the subject.

## References
1. A. A. Sardinas and G. W. Patterson, *A necessary and sufficient condition for the unique decomposition of coded messages*, IRE International Convention Record, 1953, pp. 104–108.
2. F. Blanchet-Sadri, *On unique, multiset, and set decipherability of three-word codes*, IEEE Transactions on Information Theory 47 (2001), 1745–1757, DOI: 10.1109/18.930915. https://doi.org/10.1109/18.930915
3. F. Blanchet-Sadri and T. Howell, *Note on decipherability of three-word codes*, International Journal of Mathematics and Mathematical Sciences 30 (2002), 491–504, first published 2002-05-22, DOI: 10.1155/S0161171202011729. https://doi.org/10.1155/S0161171202011729

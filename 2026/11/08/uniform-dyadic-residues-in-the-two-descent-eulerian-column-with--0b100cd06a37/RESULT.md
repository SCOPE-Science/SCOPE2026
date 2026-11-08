# Uniform dyadic residues in the two-descent Eulerian column with sharp onset

## Finding

Let \(E_n=\langle n,2\rangle\) be the number of permutations of \(\{1,\dots,n\}\) with exactly two descents (zero-based descent index), for \(n\ge3\). For each integer \(k\ge1\) define
\[
P_k=2^{k+1},\qquad N_k=\max\{3,2\lceil k/2\rceil-1\}.
\]
Then for **every** integer \(a\ge N_k\) and every \(y\in\mathbb Z/2^k\mathbb Z\),
\[
\#\{n\in\mathbb Z:a\le n<a+P_k,\ E_n\equiv y\pmod{2^k}\}=2.
\]
Exactly one of these two indices is even and the other odd. The least eventual period of \((E_n\bmod2^k)_{n\ge3}\) is \(P_k\); its sharp eventual-period starting index is \(N_k\). The same \(N_k\) is the earliest threshold after which **every** length-\(P_k\) block has the stated distribution. In particular the limiting natural density of each residue is \(2^{-k}\).

## Assumptions and scope

All indices and exponents are integers. We use \(\langle n,2\rangle\) for *two descents*, not the one-based column convention \(A(n,3)\); the underlying Eulerian triangle starts at \(n=3\). For every \(n\ge3\), inclusion-exclusion gives the classical exact identity
\[
E_n=3^n-(n+1)2^n+\binom{n+1}{2}.
\]
No assertion concerns the entries for negative indices. The modulus is a positive power of two, and all claims include \(k=1\) through \(k=4\), when the sharp onset equals the natural boundary \(n=3\).

## Proof

**1. The sharp onset.** Write \(G(n)=3^n+\binom{n+1}{2}\), for nonnegative integer \(n\). From the exact formula,
\[
E_n-G(n)=-(n+1)2^n.
\]
This correction vanishes modulo \(2^k\) for every \(n\ge N_k\). Indeed, if \(k\) is odd then \(N_k\ge k\); if \(k\) is even then \(N_k\ge k-1\), and at the possibly exceptional point \(n=k-1\) the factor \(n+1=k\) is even. For \(k\le4\), the same conclusion holds directly for all \(n\ge3\). Thus
\[
E_n\equiv G(n)\pmod{2^k}\quad(n\ge N_k).
\]
For \(k\ge5\), the immediately preceding index \(n=N_k-1\) is even and satisfies \(n<k\) and \(n+1\) odd; hence \((n+1)2^n\not\equiv0\pmod{2^k}\).

**2. An exact isometry on each parity.** For \(\varepsilon\in\{0,1\}\) and integers \(t\ge0\), put
\[
F_\varepsilon(t)=G(2t+\varepsilon)=3^\varepsilon9^t+\binom{2t+\varepsilon+1}{2}.
\]
For distinct nonnegative integers \(s,t\), set \(h=t-s\). The difference between the triangular terms is
\[
\binom{2t+\varepsilon+1}{2}-\binom{2s+\varepsilon+1}{2}
=h\,[2(t+s+\varepsilon)+1],
\]
which has valuation \(\nu_2(h)\), since the bracket is odd. By the lifting-the-exponent identity,
\[
\nu_2(9^t-9^s)=3+\nu_2(h).
\]
The exponential difference is therefore divisible by eight times the exact power of two dividing the triangular difference and cannot cancel its lowest nonzero 2-adic digit. Thus
\[
\boxed{\nu_2(F_\varepsilon(t)-F_\varepsilon(s))=\nu_2(t-s).}
\]
In particular, for each \(k\), the map \(t\bmod2^k\mapsto F_\varepsilon(t)\bmod2^k\) is well-defined and injective, hence a bijection of the finite ring. These two maps also extend to isometries of \(\mathbb Z_2\), since \(9^t\) has a continuous binomial-series extension and the valuation identity passes to limits.

**3. Every residue twice.** Fix \(k\ge1\) and any \(a\ge N_k\). The \(P_k=2^{k+1}\) consecutive indices in \([a,a+P_k)\) contain precisely \(2^k\) indices of each parity. On each parity, the associated \(t=(n-\varepsilon)/2\) runs through exactly one complete system of residues modulo \(2^k\). Step 1 replaces \(E_n\) by \(F_\varepsilon(t)\) modulo \(2^k\); Step 2 then gives one preimage of every \(y\) on each parity. This proves the distribution, with exactly two preimages in total. The natural density follows from complete eventual blocks.

**4. Least eventual period.** The congruence \(G(n+2^{k+1})\equiv G(n)\pmod{2^k}\) follows by applying Step 2 within each parity, since the corresponding \(t\)-increment is \(2^k\). Therefore \(P_k\) is an eventual period beginning at \(N_k\). But for every \(n\ge N_k\), the increment \(2^k\) corresponds within the same parity to the \(t\)-increment \(2^{k-1}\), and Step 2 yields
\[
\nu_2(G(n+2^k)-G(n))=k-1.
\]
Thus \(P_k/2\) is not an eventual period. Since every least eventual period divides any period, and \(P_k\) is a power of two, the least is precisely \(P_k\).

For \(k\ge5\), put \(n=N_k-1\). Step 1 shows \(E_n\not\equiv G(n)\pmod{2^k}\), while \(n+P_k\ge N_k\), and Step 2 gives \(G(n+P_k)\equiv G(n)\pmod{2^k}\). Hence \(E_{n+P_k}\not\equiv E_n\pmod{2^k}\). This proves that the period cannot begin earlier. The length-\(P_k\) block starting at \(n\) differs in one element from the block starting at \(n+1=N_k\), which already has two of each residue. Because the removed and added residues are distinct, this preceding block is not uniformly distributed either. It follows that the *all-future-blocks* distribution also has sharp onset \(N_k\). For \(k\le4\), sharpness follows from the domain boundary \(n\ge3\). \(\square\)

## Verification

The standalone script `verify_eulerian.py` uses only Python's standard library and checks the classical formula against an independently computed Eulerian triangle for \(3\le n\le400\). It then checks every residue in 36 complete period blocks (three starting points at each \(1\le k\le12\)), including one even and one odd preimage of each residue; it independently tests exact valuations for 15,288 same-parity pairs, the least-period obstruction, and each sharp-preperiod witness. Run `python3 verify_eulerian.py`. Its successful output begins `VERIFY_OK` and ends `one_per_parity_fiber=PASS`.

These are finite cross-checks; the unrestricted conclusion follows from the exact identities and proof above.

## Relationship to prior work

The explicit formula for \(E_n\) is classical and appears in OEIS A000460 (formula contribution dated 2002-01-22). Cao and Pan (first preprint 2006-08-23, Theorem 1.1) prove congruence divisibility for *sums over Eulerian columns at fixed row*, rather than uniform output-residue fibers for a fixed column as row length varies. Nakamura's 2015 paper treats the *normalized distribution of descents at fixed permutation size*, not the 2-adic distribution of the integer counts as permutation size varies. Castro, González, and Medina (2015) investigate valuations of Eulerian entries on congruence classes; accessible abstract/metadata describe zeros and 2-adic valuations rather than all possible target residues, but the full paper could not be inspected and this remains a priority risk. The complete all-residue fiber statement and its sharp onset were not found in the consulted OEIS entry, accessible primary statements, or targeted literature searches. None of these negative searches proves historical uniqueness.

## Limitations

This is a fixed-column and 2-adic result: it does not classify other descent columns or odd prime moduli. The isometry statement concerns the 2-adic *limiting expression* \(G\), whereas the original Eulerian sequence agrees with it only at precision \(2^k\) beyond the stated \(N_k\). The result has undergone the accompanying computational and same-document mathematical checks only; no independent mathematical audit or exhaustive historical priority check has been performed. The full text of Castro–González–Medina (2015) was inaccessible despite attempts at a public author link and publisher page; its abstract was inspected.

## References

1. OEIS A000460, Eulerian numbers, exact formula recorded 2002-01-22: https://oeis.org/A000460 .
2. H.-Q. Cao and H. Pan, *Congruences on Stirling numbers and Eulerian numbers*, initial arXiv submission 2006-08-23, https://arxiv.org/abs/math/0608564 ; later *Acta Arithmetica* **132** (2008), 315–328. Primary MSC: 11A07.
3. F. N. Castro, O. E. González, and L. A. Medina, *The p-adic Valuation of Eulerian Numbers: Trees and Bernoulli Numbers*, *Experimental Mathematics* **24** (2015), 183–195, https://doi.org/10.1080/10586458.2014.981899 .
4. N. Nakamura, *Pseudo-Normal Random Number Generation via the Eulerian Numbers*, *Josai Mathematical Monographs* **8** (2015), 85–95, https://libir.josai.ac.jp/il/user_contents/02/G0000284repository/pdf/JOS-13447777-0808.pdf .

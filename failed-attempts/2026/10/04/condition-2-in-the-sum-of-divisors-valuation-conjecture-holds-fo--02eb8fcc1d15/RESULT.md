# Condition (2) in the sum-of-divisors valuation conjecture holds for \(p=3\) and \(p=5\)

## Finding
Let \(\sigma(n)\) be the sum of the positive divisors of \(n\), and let \(\nu_p(m)\) be the \(p\)-adic valuation. Amdeberhan, Moll, Sharma, and Villamizar define condition (2), for a fixed odd prime \(p\), by requiring that every prime component \(q^a\parallel n\) satisfying
\[
\nu_p(\sigma(q^a))=\left\lceil\log_p(q^a)\right\rceil
\]
has \(q<p\).

For each
\[
p\in\{3,5\},
\]
condition (2) holds for every positive integer \(n\). In fact, the stronger local inequality
\[
\nu_p(\sigma(q^a))
\le
\left\lfloor\log_p(q^a)\right\rfloor
\]
holds for every prime \(q>p\) and every \(a\ge1\).

Thus Conjecture 1.6 of the source paper is true for the two smallest odd primes \(p=3\) and \(p=5\).

## Assumptions and scope
The proof uses the exact prime-power valuation formula of Amdeberhan, Moll, Sharma, and Villamizar. If \(p\) is odd, \(q\ne p\) is prime, \(r=\operatorname{Ord}_p(q)\), and \(a\ge1\), then
\[
\nu_p(\sigma(q^a))
=
0
\]
unless either \(q\equiv1\pmod p\) or \(r\mid a+1\). If \(q\equiv1\pmod p\), then
\[
\nu_p(\sigma(q^a))=\nu_p(a+1),
\]
and otherwise, when \(r\mid a+1\),
\[
\nu_p(\sigma(q^a))
=
\nu_p(a+1)+\nu_p(q^r-1).
\]

The claim concerns the source paper's structural condition (2), not merely the global inequality
\[
\nu_p(\sigma(n))\le\left\lceil\log_p n\right\rceil.
\]
A later paper of Zhao and Chen proves that global inequality unconditionally for every odd prime \(p\); its accessible abstract does not state the structural condition proved here.

## Proof
First take \(p=3\), and let \(q>3\) be prime.

If \(q\equiv1\pmod3\), then
\[
\nu_3(\sigma(q^a))=\nu_3(a+1).
\]
Hence
\[
3^{\nu_3(\sigma(q^a))}\le a+1<q^a,
\]
so
\[
\nu_3(\sigma(q^a))
\le
\left\lfloor\log_3(q^a)\right\rfloor.
\]

Now let \(q\equiv-1\pmod3\). Then \(\operatorname{Ord}_3(q)=2\). If \(a\) is even, the valuation is \(0\). If \(a\) is odd, then
\[
\nu_3(\sigma(q^a))
=
\nu_3(a+1)+\nu_3(q^2-1)
=
\nu_3(a+1)+\nu_3(q+1).
\]
Put
\[
A=3^{\nu_3(a+1)},\qquad B=3^{\nu_3(q+1)}.
\]
Since \(B\) is odd and divides the even number \(q+1\),
\[
B\le\frac{q+1}{2}<q.
\]
If \(a=1\), then \(A=1\), so \(AB<q=q^a\). If \(a\ge3\), then
\[
A\le a+1\le q^{a-1},
\]
and therefore again \(AB<q^a\). This proves the required floor bound for all \(q>3\).

Now take \(p=5\), and let \(q>5\) be prime.

For \(q\equiv1\pmod5\), the same argument gives
\[
5^{\nu_5(\sigma(q^a))}
\le a+1<q^a.
\]

For \(q\equiv-1\pmod5\), the order is \(2\). If \(a\) is even the valuation vanishes; if \(a\) is odd, then
\[
\nu_5(\sigma(q^a))
=
\nu_5(a+1)+\nu_5(q+1).
\]
With
\[
A=5^{\nu_5(a+1)},\qquad B=5^{\nu_5(q+1)},
\]
one has
\[
B\le\frac{q+1}{2}<q.
\]
The case \(a=1\) has \(A=1\), and for odd \(a\ge3\),
\[
A\le a+1\le q^{a-1}.
\]
Thus \(AB<q^a\).

It remains to consider \(q\equiv2\) or \(3\pmod5\), where
\[
\operatorname{Ord}_5(q)=4.
\]
Unless \(4\mid a+1\), the valuation is \(0\). If \(4\mid a+1\), then \(a\ge3\) and
\[
\nu_5(\sigma(q^a))
=
\nu_5(a+1)+\nu_5(q^4-1).
\]
Here \(5\nmid q^2-1\), so
\[
\nu_5(q^4-1)=\nu_5(q^2+1).
\]
Put
\[
A=5^{\nu_5(a+1)},\qquad B=5^{\nu_5(q^2+1)}.
\]
Since \(B\) is odd and divides the even number \(q^2+1\),
\[
B\le\frac{q^2+1}{2}<q^2.
\]
Also \(q\ge7\), \(a\ge3\), and
\[
A\le a+1\le q^{a-2}.
\]
Therefore \(AB<q^a\), which gives the floor bound.

Finally, if \(q=p\), then
\[
\sigma(p^a)\equiv1\pmod p,
\]
so \(\nu_p(\sigma(p^a))=0\), while \(\lceil\log_p(p^a)\rceil=a>0\). Thus an equality component cannot have \(q=p\), and the proved floor bound excludes every \(q>p\). Any equality component must therefore satisfy \(q<p\), which is exactly condition (2).

## Verification
The proof is symbolic and covers all exponents and primes in the stated cases. The accompanying `verify.py` is a regression check, not a substitute for the proof: it independently computes \(\sigma(q^a)\) for primes \(q<500\) and \(1\le a\le80\), and confirms the local floor inequality for \(p=3\) and \(p=5\).

## Relationship to prior work
The 2020 preprint of Amdeberhan, Moll, Sharma, and Villamizar states Conjecture 1.6: for each fixed odd prime \(p\), every positive integer should satisfy condition (1) or condition (2). Their Theorem 1.2 supplies the prime-power valuation formula used above.

Zhao and Chen later proved the global consequence
\[
\nu_p(\sigma(n))\le\left\lceil\log_p n\right\rceil
\]
unconditionally for every odd prime \(p\). That later theorem removes the need for the source paper's technical conditions when proving the global bound, but it does not, from the accessible abstract, assert condition (2) itself. The result here is therefore a structural verification of the original technical conjecture for \(p=3\) and \(p=5\), not a new proof of the already-known global inequality.

Targeted searches using the source title, Conjecture 1.6, conditions (1) and (2), the primes \(3\) and \(5\), and the local prime-power inequality did not locate a prior statement of these two structural cases.

## Limitations
The argument does not treat \(p\ge7\). For larger \(p\), multiplicative orders can introduce cyclotomic factors whose degree is large enough that the elementary size argument above no longer closes in the same way.

The full text of the later Zhao--Chen paper was not accessible through the lawful open sources inspected here; only its abstract, metadata, and references were available. Consequently there is a residual originality risk that its full proof may contain the same structural \(p=3\) or \(p=5\) observation even though the accessible abstract states only the unconditional global inequality.

## References
1. T. Amdeberhan, V. H. Moll, V. Sharma, and D. Villamizar, “Arithmetic properties of the sum of divisors,” arXiv:2007.03088v1, first posted 6 July 2020; later published in *Journal of Number Theory* 223 (2021), 325--349.
2. J. Zhao and Y. Chen, “\(p\)-adic Valuation of the Sum of Divisors,” *Frontiers of Mathematics* 20 (2025), 795--827, DOI 10.1007/s11464-023-0154-2.

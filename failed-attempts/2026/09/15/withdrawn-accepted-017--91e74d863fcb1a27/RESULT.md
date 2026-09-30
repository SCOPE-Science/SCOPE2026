# Exact stable 3-primary exponent of the type-2 Smith–Toda spectrum V(1)

## Context

Let $p=3$ and work in the $3$-local stable homotopy category. Let $V(0)=S/3$ be
the mod-$3$ Moore spectrum, the cofiber of $3:S\to S$, so
$BP_*V(0)=BP_*/(3)$. Let $v_1:\Sigma^4V(0)\to V(0)$ be a $v_1$-self map
inducing multiplication by $v_1$ on $BP_*/3$, and let
$V(1)=\mathrm{cof}(v_1)$ be the type-2 Smith–Toda complex, so
$BP_*V(1)=BP_*/(3,v_1)$. Define the stable $3$-primary exponent by
$\exp_3(V(1))=\min\{e\ge 0\mid 3^e\text{ annihilates }\pi_k(V(1)_{(3)})
\text{ for all }k\}$, with value infinity if no such $e$ exists.
The question is whether this exponent is finite, whether $9\cdot\mathrm{id}=0$
($e\le 2$), and whether $3\cdot\mathrm{id}=0$ ($e=1$) or some stem contains an
element of order $9$ with $9$ killing all stems ($e=2$).

## Definitions

- $S$: $3$-local sphere spectrum; $[S,S]=\mathbb{Z}_{(3)}$.
- $V(0)$: cofiber $S\xrightarrow{3}S\xrightarrow{i_0}V(0)
  \xrightarrow{d_0}S^1$.
- $V(1)$: cofiber $\Sigma^4V(0)\xrightarrow{v_1}V(0)
  \xrightarrow{i_1}V(1)\xrightarrow{d_1}\Sigma^5V(0)$.
- $a_X=3\cdot\mathrm{id}_X$: central natural endomorphism; for
  $f:X\to Y$, $f\circ a_X=a_Y\circ f$.
- $\pi_k(X)=[S^k,X]$ denotes $3$-local stems.

## Result

For every choice of $v_1$ (including the split null case),
$3\cdot\mathrm{id}_{V(1)}=0$ in the $3$-local stable homotopy category.
Consequently $9\cdot\mathrm{id}_{V(1)}=0$, every $3$-local stem
$\pi_k(V(1))$ is an $\mathbf{F}_3$-vector space, no stem contains an element
of order $9$, $V(1)\not\simeq\ast$, and $\exp_3(V(1))=1$ exactly.
In particular finiteness holds with $e\le 2$ and the alternative $e=2$
does not occur.

## Proof / Evidence

Work $3$-locally. First a triangulated factorization lemma: for an exact
triangle $X\to Y\to C\to\Sigma X$ with $a=3\cdot\mathrm{id}$ and
$a_X=a_Y=0$, writing $c=a_C$ gives $c\circ i=0$ and $d\circ c=0$ by
naturality, hence $c=f\circ d=i\circ g$ and $c^2=f\circ(d\circ i)\circ g=0$,
i.e. $9\cdot\mathrm{id}_C=0$; if moreover the relevant $[C,Y]$ or
$[\Sigma X,C]$ vanishes then $c=0$.

For $V(0)$, $c_0=a_{V(0)}$ satisfies $c_0\circ i_0=0$ and
$d_0\circ c_0=0$, so $c_0=i_0\circ g_0$ with $g_0:V(0)\to S$.
Applying $[-,S]$ gives $[S^1,S]\to[V(0),S]\to[S,S]\xrightarrow{\times3}[S,S]$
with $[S^1,S]=\pi_1S_{(3)}=0$ (since $\pi_1S=\mathbb{Z}/2$) and $\times3$
injective on $\mathbb{Z}_{(3)}$, so $[V(0),S]=0$, $g_0=0$, and
$3\cdot\mathrm{id}_{V(0)}=0$; $\pi_0V(0)=\mathbb{Z}/3\ne0$ so
$V(0)\not\simeq\ast$.

Hence for $V(1)$ with $c_1=a_{V(1)}$, vanishing of $a_{V(0)}$ gives
$c_1\circ i_1=0$, $d_1\circ c_1=0$, $c_1=i_1\circ g=f\circ d_1$ and
$c_1^2=0$, i.e. $9\cdot\mathrm{id}_{V(1)}=0$ and $\exp_3\le2$.

Low $3$-local stems $\pi_1S=\pi_2S=0$, $\pi_3S=\mathbb{Z}/3$ (from
$\mathbb{Z}/24$), $\pi_4S=\pi_5S=0$, $\pi_6S=0$ (from $\mathbb{Z}/2$) give
$\pi_0V(0)=\mathbb{Z}/3$, $\pi_1V(0)=\pi_2V(0)=0$,
$\pi_3V(0)=\mathbb{Z}/3$, $\pi_4V(0)\cong\ker(3:\pi_3S\to\pi_3S)
=\mathbb{Z}/3$, $\pi_5V(0)=\pi_6V(0)=0$.
From $[-,S^1]$ and $[-,V(0)]$ long exact sequences,
$[V(0),S^1]\cong\mathbb{Z}/3$, $[V(0),V(0)]\cong\mathbb{Z}/3$,
$[\Sigma^4V(0),V(0)]\cong\mathbb{Z}/3$ via $\pi_4V(0)$, and
$[\Sigma^5V(0),V(0)]=0$ since $\pi_5V(0)=\pi_6V(0)=0$.

Applying $[-,V(0)]$ to the $V(1)$ triangle gives
$0=[\Sigma^5V(0),V(0)]\to[V(1),V(0)]\to[V(0),V(0)]
\xrightarrow{v_1^*}[\Sigma^4V(0),V(0)]$, so $[V(1),V(0)]\cong\ker v_1^*$.
If $v_1=0$ then $V(1)\simeq V(0)\vee\Sigma^5V(0)$ has $3\cdot\mathrm{id}=0$
directly. Otherwise $v_1\ne0$ is essential (nonzero on $BP_*/3$), so
$v_1^*:\mathbb{Z}/3\to\mathbb{Z}/3$ sends $\mathrm{id}$ to a nonzero element
and is an isomorphism; hence $\ker v_1^*=0$ and $[V(1),V(0)]=0$.
Since $c_1=i_1\circ g$ with $g:V(1)\to V(0)$, $g=0$ gives
$3\cdot\mathrm{id}_{V(1)}=0$. This annihilates every
$[S^k,V(1)]=\pi_k(V(1))$, so $e\le1$; $BP_*V(1)=BP_*/(3,v_1)\ne0$
(equivalently $H_0(V(1);\mathbf{F}_3)\ne0$) gives $V(1)\not\simeq\ast$,
so $e\ge1$ and $e=1$ exactly with no order-$9$ stems.

## Limitations

The argument uses classical low-degree $3$-local stable stems through
$\pi_6$ and the existence/nontriviality of $v_1$ on $BP$-homology as given;
it computes no higher stems of $V(1)$ and addresses no $p>3$ analogue.
It is an integral statement about $3\cdot\mathrm{id}_{V(1)}$; $L_2$-local
or $E_2$-level $\mathbf{F}_3$-structure alone does not imply it because of
possible hidden $\mathbb{Z}/9$ extensions, which this proof rules out.

## Reproducibility

All steps are elementary cofiber long exact sequences from the two
defining triangles plus standard $3$-localizations
$\pi_1S=\mathbb{Z}/2\mapsto0$, $\pi_3S=\mathbb{Z}/24\mapsto\mathbb{Z}/3$,
$\pi_6S=\mathbb{Z}/2\mapsto0$. No computer calculation is required; any
checker can recompute the four endomorphism groups and the kernel
$\ker v_1^*$ above. The null-$v_1$ split case is checked separately.

## References

- Toda–Smith complex definitions: $BP_*(V(n))=BP_*/(p,\dots,v_n)$; nLab
  and standard chromatic references.
- K. Shimomura, The homotopy groups of the $L_2$-localized Toda–Smith
  spectrum $V(1)$ at the prime $3$, Trans. Amer. Math. Soc. 349 (1997).
- M. Behrens, S. Pemmaraju, On the existence of the self map $v_2^9$ on
  the Smith–Toda complex $V(1)$ at the prime $3$ (arXiv:math/0303223).
- K. Shimomura and M. Shimomura, On products of beta and gamma elements in
  the homotopy of the first Smith–Toda spectrum, Geom. Topol. 24 (2024).

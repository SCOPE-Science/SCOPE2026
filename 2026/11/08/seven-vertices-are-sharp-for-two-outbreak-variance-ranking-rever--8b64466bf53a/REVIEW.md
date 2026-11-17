# Independent mathematical audit

## correctness

PASS

The rooted cluster variance polynomial follows from indicators along unique open s-v paths: V_s(p)=sum_{u,v}p^{(d(s,u)+d(s,v)+d(u,v))/2}-(sum_v p^{d(s,v)})^2. All seed differences factor p(1-p). Source check.py exhausts Prüfer codes for n<=7 and canonical unrooted shapes, then transforms Q by z/(1+z) and uses exact integer Descartes sign variations to rule out >1 crossings for n<=6; exactly three n7 representatives allow 2 signs and constitute two marked-pair isomorphism classes. Each exceptional witness has signs (-,+,-) or (+,-,+) at 0,1/2,1, giving exactly two distinct simple roots by IVT plus Descartes upper bound. Independent NetworkX tree enumeration and exact SymPy open-interval real-root checks reproduced 0 two-reversal pairs through n6 and exactly 3 representative pairs at n7. Independent 64-mask expectation expansion in source checks the displayed quartic. No larger-tree bound is asserted.

## originality

PASS

Natural two-switch variance-ranking cutoff for root epidemics remains distinct from well-studied mean source rankings and global random-root variance extremization; published generic variance formulas do not imply the exact seven-vertex, two marked-class finding without complete computation.

## value

PASS

First nontrivial threshold for *two* strict variance reversals of rooted epidemic cluster sizes on a tree and complete marked-tree census at that threshold is a motivated exact boundary in reliability and uncertainty ranking, independent of (and structurally subtler than) mean crossings. Two rigorously isolated intervals are exact finite mathematical facts of ongoing usefulness.

The dated certificate retains the supplied scientific assessment, sources and limitations.

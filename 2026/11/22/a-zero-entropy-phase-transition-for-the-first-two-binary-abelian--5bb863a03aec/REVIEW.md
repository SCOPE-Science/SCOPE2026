# Independent mathematical audit

## correctness

PASS

After excluding 000 and 111, an ordinary period-two Abelian cube consists exactly of three consecutive blocks in {01,10}. This gives a memory-five graph. Independent direct-window reconstruction (independent_check.py) obtained the displayed 16 vertices and 18 edges, with a direct word check through n=16 and path counts through n=200; the frozen checker scripts and VERIFICATION.md were read, not executed. The graph itself proves the all-length formula: at path length >=3 one has six cycle-only paths, two entry-only and two exit-only paths, with two further paths of lengths 4 mod 3 using both an entry and an exit. The remaining transient paths have at most two edges. These phases give 10+2*1_{3 divides n} from n=8; the short counts and generating function follow. With no intercycle connection, no transient edge can occur on a path extending in both directions; the two three-cycles give precisely six bi-infinite points. The full linear-word census includes transient words, so it is not identical to the set of factors of the two-sided shift, although both have entropy zero.

## originality

PASS

The standard finite-type enumeration method is not new. The exact ordinary binary short-period language and the six-point classification are distinct from the closest inspected results for other restrictions and alphabets.

## value

PASS

Tests the earliest natural cutoffs of ordinary Abelian-cube periods, not a selected isolated word length. At cutoff one, concatenations of 01 and 10 already give exponentially many extendible words; adding period two reduces the entire two-sided shift to six points. The index-sensitive finite census also records the remaining boundary transients, which entropy alone misses. The result gives a useful complete local baseline for comparison across periods and alphabets.

The dated certificate retains the supplied scientific assessment, sources and limitations.

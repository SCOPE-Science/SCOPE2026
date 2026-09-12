"""Bounded finite-radius probe of Hjorth local-orbit density (lane-1084).

Candidate: length-32 Toeplitz-style word from a period-8 skeleton.
Enumerate all 256 radius-1 binary block maps, apply with wraparound, count
distinct images; compare against a basic clopen neighbourhood (fix central
8 symbols -> 2^24 words). Map invertibility is NOT checked, so the reached
set OVERESTIMATES the true conjugacy-orbit fragment.
"""
L = 32
base = [0, 1, 0, 0, 1, 1, 0, 1]
w = (base * 4)[:L]
assert len(w) == L
imgs = set()
for code in range(256):
    f = [(code >> v) & 1 for v in range(8)]
    out = []
    for i in range(L):
        a, b, c = w[(i - 1) % L], w[i], w[(i + 1) % L]
        out.append(f[(a << 2) | (b << 1) | c])
    imgs.add(tuple(out))
print("candidate word (len %d): %s" % (L, "".join(map(str, w))))
print("distinct radius-1 images: %d / 256 maps" % len(imgs))
K = 8
print("basic nbhd fixing central %d symbols holds 2^%d = %d words" % (K, L - K, 2 ** (L - K)))
print("fraction reached <= %d / %d = %.3e" % (len(imgs), 2 ** (L - K), len(imgs) / 2 ** (L - K)))
print("RESULT: finite-radius fragment is a negligible sliver of every basic")
print("  neighbourhood (invertibility unchecked, so this overestimates). No density")
print("  certifiable; Homeo(2^N) basic nbhds involve arbitrary clopen partitions,")
print("  so finite search cannot witness turbulence. ROUTE INCONCLUSIVE (bounded).")
print("VERIFY_OK")

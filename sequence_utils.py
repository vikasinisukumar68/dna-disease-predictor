def analyze_sequence(sequence):
    # Dummy simple rules for detecting variations for demo purpose
    # In reality, this would require complex bioinformatics analysis
    analysis = {
        "SNV": False,
        "Indel": False,
        "Repeat": False,
        "CNV": False,
        "SpliceSite": False
    }

    # SNV detection: look for single base changes (simulate by presence of 'A' followed by 'G')
    if 'AG' in sequence or 'GA' in sequence:
        analysis['SNV'] = True

    # Indel detection: look for repeated short insertion (simulate 'ATTAT' pattern)
    if 'ATTAT' in sequence or 'TATTA' in sequence:
        analysis['Indel'] = True

    # Repeat detection: look for trinucleotide repeats like CAGCAG or CGGCGG
    repeats = ['CAGCAG', 'CGGCGG', 'GAA GAA'.replace(' ', '')]
    for rep in repeats:
        if rep in sequence:
            analysis['Repeat'] = True
            break

    # CNV detection: simulate by presence of 'EXTRA' or 'MISS' substring (not real DNA, just demo)
    if 'EXTRA' in sequence or 'MISS' in sequence:
        analysis['CNV'] = True

    # SpliceSite mutation: simulate by 'GTAG' or 'AGGT' pattern (common splice site motifs)
    splice_patterns = ['GTAG', 'AGGT']
    for sp in splice_patterns:
        if sp in sequence:
            analysis['SpliceSite'] = True
            break

    return analysis
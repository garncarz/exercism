def distance(dna1, dna2):
    if len(dna1) != len(dna2):
        raise ValueError

    return sum(map(lambda nucl: int(nucl[0] != nucl[1]), zip(dna1, dna2)))

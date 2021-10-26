def change_strand(strand):
    reverse_strand = str()
    elements = {"A": "T", "G": "C", "T": "A", "C": "G"}

    for element in strand:
        reverse_strand += elements[element]

    return reverse_strand


# module for all the function
def sticking_time(file_name):
    with open(file_name) as file:
        original_plasmid = file.readline().strip("\n")
        restriction_site = file.readline().strip("\n")
        GFP = file.readline().strip("\n")
        left_GFP_restriction_site, right_GFP_restriction_site = file.readline().strip("\n").split()

    # Restriction sites
    restriction_site_index = original_plasmid.index(restriction_site) + 1
    left_GFP_restriction_index = GFP.index(left_GFP_restriction_site) + 1
    right_GFP_restriction_index = GFP.index(right_GFP_restriction_site) + 1

    # Adding values to output
    result = original_plasmid[:restriction_site_index]
    result += GFP[left_GFP_restriction_index: right_GFP_restriction_index]
    result += original_plasmid[restriction_site_index:]

    return result


def main():
    file_name = input()
    result = sticking_time(file_name)

    print(f"{result}\n{change_strand(result)}")


if __name__ == '__main__':
    main()

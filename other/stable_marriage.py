from typing import List, Dict, Tuple

"""
    The Stable Marriage Problem involves matching two equal-sized groups (men and women)
    based on individual preferences. The goal is to find a *stable pairing*, where no pair would
    rather be with each other than their current partners.

    refer to the wikepedia link to know more about the algorithm
    https://en.wikipedia.org/wiki/Stable_marriage_problem#:~:text=The%20stable%20marriage%20problem%20has,other%20than%20their%20current%20partners.
"""


def stable_marriage(
    men: List[str], women: List[str], preferences: Dict[str, List[str]]
) -> Dict[str, str]:
    """Finds a stable marriage pairing.

    Args:
        men: List of men's names.
        women: List of women's names.
        preferences: Dictionary of preferences for each man and woman.

    Returns:
        A dictionary representing the stable marriage pairs.
    """

    # Initialize all men and women as free
    free_men = men.copy()
    engagements = {woman: None for woman in women}  # Initialize engagements for women
    proposals = {man: 0 for man in men}  # Track proposals made by each man

    while free_men:
        # Select the first free man
        man = free_men[0]
        # Get the next woman to propose to
        woman = preferences[man][proposals[man]]
        proposals[man] += 1  # Increment proposal count

        if engagements[woman] is None:
            # If woman is free, engage
            engagements[woman] = man
            free_men.remove(man)  # Man is no longer free
        else:
            # If woman is already engaged
            current_partner = engagements[woman]
            # Check if she prefers the new man
            if preferences[woman].index(man) < preferences[woman].index(
                current_partner
            ):
                # She prefers the new man
                engagements[woman] = man
                free_men.remove(man)  # Man is no longer free
                free_men.append(current_partner)  # The current partner becomes free
            # If she prefers her current partner, do nothing

    return engagements


# Example usage
men = ["A", "B", "C"]
women = ["X", "Y", "Z"]
preferences = {
    "A": ["X", "Y", "Z"],
    "B": ["Y", "X", "Z"],
    "C": ["Z", "X", "Y"],
    "X": ["A", "B", "C"],
    "Y": ["B", "A", "C"],
    "Z": ["C", "A", "B"],
}

result = stable_marriage(men, women, preferences)
print(f"Stable marriages: {result}")

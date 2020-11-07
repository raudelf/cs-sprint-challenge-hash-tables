def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    weight_dict = {}

    for index, weight in enumerate(weights):
        weight_dict[weight] = index

    for index, weight in enumerate(weights):
        diff = limit - weight

        if diff in weight_dict:
            index_2 = weight_dict[diff]

            if index_2 > index:
                return (index_2, index)
            else:
                return (index, index_2)

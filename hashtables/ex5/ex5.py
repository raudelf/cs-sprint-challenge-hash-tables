# Your code here


def finder(files, queries):
    """
    YOUR CODE HERE
    """
    cache = {}
    direct_results = []

    for directory in files:
        file_name = directory.split('/')[-1]

        if file_name in cache:
            cache[file_name].append(directory)
        else:
            cache[file_name] = [directory]

    for file_name in queries:
        if file_name in cache:
            result = cache[file_name]

            for directory in result:
                direct_results.append(cache[file_name])

    return direct_results


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))

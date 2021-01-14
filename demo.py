

from depLength import depLength as dl

sentences = """
John threw out the trash. John threw the trash out. John threw out the old trash sitting in the kitchen. John threw the old trash sitting in the kitchen out.
"""

res = dl.DepLength(sentences)
print(res.sdl())

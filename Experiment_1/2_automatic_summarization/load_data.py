# -*- coding: utf-8 -*-
from os import listdir
import tqdm


# load doc into memory
def load_doc(filename):
    # open the file as read only
    file = open(filename, encoding='utf-8')
    # read all text
    text = file.read()
    # close the file
    file.close()
    return text


# split a document into news story and highlights
def split_story(doc):
    # find first highlight
    index = doc.find('@highlight')
    # split into story and highlights
    story, highlights = doc[:index], doc[index:].split('@highlight')
    # strip extra white space around each highlight
    highlights = [h.strip() for h in highlights if len(h) > 0]
    return story, highlights


def load_stories(directory, num_stories=-1):
    """load stories
    
    Args:
        directory(str): the path of cnn_stories
        num_stories(int): NUM of stories to use

    Returns:
        all_stories(list): A list of dict, dict contains `story`(str) and `highlights`(a list of str)
    """
    all_stories = list()
    filenames = listdir(directory)
    if num_stories > -1:
        filenames = filenames[:num_stories]

    for name in tqdm.tqdm(filenames):
        filename = directory + '/' + name
        # load document
        doc = load_doc(filename)
        # split into story and highlights
        story, highlights = split_story(doc)
        # store
        all_stories.append({'story': story, 'highlights': highlights})

    return all_stories


if __name__ == '__main__':
    # load stories
    directory = 'data/cnn_stories_tokenized/'
    stories = load_stories(directory, 10000)
    print('Loaded Stories %d' % len(stories))

    print(stories[4]['story'])
    print(stories[4]['highlights'])

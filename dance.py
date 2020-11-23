
class DancePart(object):
    """ DancePart for Nao dance includes lists of names, times, and keys for Python
        simplified dances exported from Choreographe"""

    def __init__(self, part_length, pause_length, names, times, keys):
        super(DancePart, self).__init__()
        self.part_length = part_length
        self.pause_length = pause_length
        self.names = names
        self.times = times
        self.keys = keys

    def get_part_length(self):
        return self.part_length

    def get_pause_length(self):
        return self.pause_length

    def get_names(self):
        return self.names

    def get_times(self):
        return self.times

    def get_keys(self):
        return self.keys


class Dance(object):
    """ Nao robot dance. The attribute num_parts is the number of parts in the dance.
        The parts attribute is a list of DanceParts"""

    def __init__(self, song_name, num_parts, parts):
        super(Dance, self).__init__()
        self.song_name = song_name
        self.num_parts = num_parts
        self.parts = parts

    def get_part(self, part_num):
        return self.parts[part_num]

    def get_song_name(self):
        return self.song_name

    def get_num_parts(self):
        return self.num_parts

    def get_parts(self):
        return self.parts

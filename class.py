class RemoteControl:

    def __init__(self):
        self.channels = ['Marvel','DC','Anime','Cartoon','Pixel']
        self.index = -1

    def __iter__(self):
         return self

    def __next(self):
        self.index += 1
        if self.index == len(self.channels):
            #raise StopIteration
            self.index=0
        return self.channels[self.index]
r = RemoteControl()
itr = iter(r)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
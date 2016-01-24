def answer(chunk, word):
    indicator = len(chunk)
    wordlen = len(word)    
    while word in chunk:
        find = chunk.rindex(word)
        chunk = chunk[:find]+chunk[find+wordlen:]
    
    
    new = []
    for element in (word[:i]+word+word[i:] for i in range(1,len(word))):
        ffind = element.rindex(word)
        element = element[:ffind]+element[ffind+wordlen:]
        if element != word:
            new = new+[element]
            
    if new:
        while any((thing in chunk for thing in new)):
            for thing in new:
                fffind = chunk.rfind(thing)
                if fffind != -1:
                    chunk = chunk[:fffind]+chunk[fffind+wordlen:]
                
    return chunk
                    

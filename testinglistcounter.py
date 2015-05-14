things = ['item1', 'item2', 'aitem3']
numb = things.index('item1')
things.remove('item1')
things.insert(numb, '1. item1')
numb = things.index('item2')
things.remove('item2')
things.insert(numb, '2. item2')
numb = things.index('aitem3')
things.remove('aitem3')
things.insert(numb, '3. aitem3')
things.sort
print things

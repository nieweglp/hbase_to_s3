hbase shell
create 'books', 'info', 'analytics'
put 'books', 'In Search of Lost Time', 'info:author', 'Marcel Proust'
put 'books', 'In Search of Lost Time', 'info:year', '1922'
put 'books', 'In Search of Lost Time', 'analytics:views', '3298'
put 'books', 'Godel, Escher, Bach', 'info:author', 'Douglas Hofstadter'
put 'books', 'Godel, Escher, Bach', 'info:year', '1979'
put 'books', 'Godel, Escher, Bach', 'analytics:views', '820'
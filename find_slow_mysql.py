import gzip
import shutil

num = 1
# Extract the contents of the archive to a file
while num <= 7:
    with gzip.open('/path/mysql-slow.log.'+str(num)+'.gz', 'rb') as f_in:
        with open('/tmp/file.txt', 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
    num += 1

with open('/path/tmp/result.txt', 'w') as res:
    with open('/tmp/file.txt', 'r') as file:
        arr = file.readlines()

        for line in arr:
            if line.count('# Query_time:'): # Specify search parameters
                res.write('\n\n'+line[2:(line.index('L')-2)]+'\n')
            if line.count('SET') or line.count('SELECT') or line.count('use'): # Specify search parameters
                res.write(line)




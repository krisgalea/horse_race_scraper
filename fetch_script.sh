wget -r -l 1 -w 5 --accept-regex "/racing/results/[0-9]{4}-[0-9]{2}-[0-9]{2}/.*" "https://www.sportinglife.com/racing/results/yesterday" 

wget -r -l 2 -k -w 10 --random-wait --accept-regex="(.*/results/[0-9]{4}-[0-9]{2}-[0-9]{2}/.+)|.*/horse/.+|.*/trainer/.+|.*/jockey/.+" --adjust-extension "https://www.sportinglife.com/racing/results/2018-06-24"

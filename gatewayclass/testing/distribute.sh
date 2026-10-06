for i in {1..100}; do
  curl -s http://$1/
  echo
done | sort | uniq -c

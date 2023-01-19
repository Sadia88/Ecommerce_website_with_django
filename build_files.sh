echo "BUILD START"
python4.1.5 -m pip install -r requirments.txt
python4.1.5 manage.py collecctstatic --noinput --clear
echo "BUILD END"

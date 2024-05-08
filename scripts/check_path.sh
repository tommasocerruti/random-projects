#script checking what paths included in $PATH do not exist

for dir in $(echo $PATH | tr ':' '\n'); do
    if [ ! -d "$dir" ]; then
        echo "Directory '$dir' does not exist."
    fi
done

OWNER=three0-s
REPOSITORY=myga-satellite
ACCESS_TOKEN=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
VERSION=oiltank
curl --data '{"tag_name": "oiltank-dataset",
                "target_commitish": "master",
                "name": "oiltank-dataset",
                "body": "Release of version $VERSION",
                "draft": false,
                "prerelease": false}' \
    https://api.github.com/repos/$OWNER/$REPOSITORY/releases \
    --header "Authorization: Bearer $ACCESS_TOKEN" \

# Nono Heryana | Academic Jekyll Website

A responsive Jekyll academic website for GitHub Pages.

## Local development

Install Ruby and Bundler, then:

```bash
bundle install
bundle exec jekyll serve
```

Visit http://127.0.0.1:4000.

## Deploy to GitHub Pages

1. Create a GitHub repository and push all project files.
2. In Settings > Pages, select Deploy from a branch, branch `main`, folder `/ (root)`.
3. For a project repository (not `<username>.github.io`), set `baseurl: "/repository-name"` in `_config.yml`. Set `url: "https://<username>.github.io"`.
4. For a user site, keep `baseurl: ""` and set `url: "https://<username>.github.io"`.
5. Set repository variable `ORCID_ID` in Settings > Secrets and variables > Actions > Variables.
6. In Actions, run `Sync ORCID publications` manually once. It will then run weekly.
7. Ensure Actions has permission to write repository contents if the workflow cannot push.

## Customize

- `_data/profile.yml`: academic identity and links.
- `_data/teaching.yml`: courses.
- `_posts/`: blog posts.
- `_projects/`: optional project markdown files (create directory).
- `assets/files/cv.pdf`: verified PDF CV.
- `index.html`: homepage.
- `assets/css/style.css`: design system.

## Publication metadata limitations

ORCID may not include all publications and often omits author lists. This importer intentionally leaves authors blank instead of inventing them. Check records and DOI against publisher metadata. Public ORCID visibility is required. Never put private API credentials in the repository.

# Vantage Sauna Co. marketing site

One self-contained page: `index.html` (inline CSS, inline JS, inline SVG, no raster images, no external scripts). The only external resources are the Fraunces and Inter stylesheets from Google Fonts; the page falls back to system serif and sans-serif faces without them.

## Serve it locally

From this folder:

```sh
cd website
python3 -m http.server 8000
```

Then open <http://localhost:8000/>. Opening `index.html` directly as a file also works.

When served locally there is no `window.claude`, so the "Request a site assessment" form falls back to opening a prefilled `mailto:` link to `hello@vantagesauna.example` and shows a thank-you state with a copyable summary of the request.

## Publishing as a Claude artifact

Publish `index.html` with the Artifact tool and pass this `capabilities` object so the form can save submissions:

```json
{
  "db": {
    "rules": [
      { "path": "leads", "read": "admin", "write": "admin" },
      { "path": "leads/{self}", "read": "view", "write": "interact" }
    ]
  },
  "user": {}
}
```

Submissions are written to the `leads` collection, one document per submitter (`leads/<viewer id>`), with the latest request at the top level and earlier requests from the same person in a `history` array. Only the artifact owner and Editors can read the collection; each submitter can read only their own entry. Read leads with the `ArtifactData` tool (`list` on collection `leads`).

Only signed-in members of the owner's organisation at Contributor level or above can write to the store. Anyone else who submits the form (outside visitors, signed-out visitors, or anyone whose write is refused) gets the same `mailto:` and copy-summary fallback as the local version.

## Placeholder links

Two placeholder `href` values need real URLs before launch:

| Placeholder          | Where it appears                                                        |
|----------------------|-------------------------------------------------------------------------|
| `DESIGN_PLANS_URL`   | Hero button "Explore the 3D design plans"; footer link "3D design plans" |
| `INVESTOR_DECK_URL`  | Footer link "Investor deck"                                             |

Search the file for each string and replace it.

## Theme

The nav has a light/dark toggle that sets `data-theme` on `<html>` and remembers the choice in `localStorage` (key `vantage-theme`). With no stored choice the page follows the system theme.

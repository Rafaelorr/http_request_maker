# Standard response fields
## Accept-CH

[RFC 8942, experimental] Requests HTTP Client Hints.

For example: `Accept-CH: UA, Platform`

## Access-Control-Allow-Origin, Access-Control-Allow-Credentials, Access-Control-Expose-Headers, Access-Control-Max-Age, Access-Control-Allow-Methods, Access-Control-Allow-Headers

[RFC 7480, permanent] Specifying which web sites can participate in cross-origin resource sharing.

For example: `Access-Control-Allow-Origin: *`

## Accept-Patch

[RFC 5789, permanent] Specifies which patch document formats this server supports.

For example: `Accept-Patch: text/example;charset=utf-8`

## Accept-Ranges

[RFC 9110, permanent] What partial content range types this server supports via byte serving.

For example: `Accept-Ranges: bytes`

## Age

[RFC 9111, permanent] The age the object has been in a proxy cache in seconds.

For example: `Age: 12`

## Allow

[RFC 9110, permanent] Valid methods for a specified resource. To be used for a 405 Method not allowed.

For example: `Allow: GET, HEAD`

## Alt-Svc

[RFC 7838, permanent] A server uses "Alt-Svc" header (meaning Alternative Services) to indicate that its resources can also be accessed at a different network location (host or port) or using a different protocol. When using HTTP/2, servers should instead send an ALTSVC frame.

For example: `Alt-Svc: http/1.1="http2.example.com:8001"; ma=7200`

## Cache-Control

[RFC 9111, permanent] Tells all caching mechanisms from server to client whether they may cache the response. A numeric value is in seconds.

If a web server responds with Cache-Control: no-cache, then a web browser or other caching system (intermediate proxies) must not use the response to satisfy subsequent requests without first checking with the originating server (this process is called validation). This header field is part of HTTP/1.1, and is ignored by some caches and browsers. It may be simulated by setting the Expires HTTP/1.0 header field value to a time earlier than the response time. Notice that no-cache is not instructing the browser or proxies about whether or not to cache the content. It tells the browser and proxies to validate the cache content with the server before using it (this is done via If-Modified-Since, If-Unmodified-Since, If-Match, and If-None-Match). Sending a no-cache value thus instructs a browser or proxy to not use the cache contents merely based on "freshness criteria" of the cache content. Another common way to prevent old content from being shown to the user without validation is Cache-Control: max-age=0 which instructs the user agent that the content is stale and should be validated before use.

The value no-store instructs a browser to not cache the response, yet the browser is allowed to cache it none-the-less. In particular, the HTTP/1.1 definition draws a distinction between history stores and caches. If the user navigates back to a previous page, a browser may show a page that was stored on disk in the history store. This is correct behavior according to the specification. Many user agents provide different behavior in loading pages from the history store or cache depending on whether the protocol is HTTP or HTTPS.

For example: `Cache-Control: max-age=3600`

## Connection

[RFC 9110, permanent] Control options for the current connection and list of hop-by-hop response fields. Must not be used with HTTP/2.

For example: `Connection: close`

## Content-Disposition

[RFC 2616, 4021, 6266, permanent] An opportunity to raise a "File Download" dialogue box for a known MIME type with binary format or suggest a filename for dynamic content. Quotes are necessary with special characters.

For example: `Content-Disposition: attachment; filename="fname.ext"`

## Content-Encoding

[RFC 9110, permanent] The type of encoding used on the data. See HTTP compression.

For example: `Content-Encoding: gzip`

## Content-Language

[RFC 9110, permanent] The natural language or languages of the intended audience for the enclosed content.

For example: `Content-Language: da`

## Content-Length

[RFC 9110, permanent] The length of the response body in octets (8-bit bytes).

For example: `Content-Length: 348`

## Content-Location

[RFC 9110, permanent] An alternate location for the returned data.

For example: `Content-Location: /index.htm`

## Content-MD5

[RFC 1544, 1864, 4021, obsolete] A Base64-encoded binary MD5 sum of the content of the response.

For example: `Content-MD5: Q2hlY2sgSW50ZWdyaXR5IQ==`

## Content-Range

[RFC 9110, permanent] Where in a full body message this partial message belongs.

For example: `Content-Range: bytes 21010-47021/47022`

## Content-Type

[RFC 9110, permanent] The MIME type of this content.

For example: `Content-Type: text/html; charset=utf-8`

## Date

[RFC 9110, permanent] The date and time that the message was sent (in "HTTP-date" format as defined by RFC 9110).

For example: `Date: Tue, 15 Nov 1994 08:12:31 GMT`

## Delta-Base

[RFC 3229, permanent] Specifies the delta-encoding entity tag of the response.

For example: `Delta-Base: "abc"`

## ETag

[RFC 9110, permanent] An identifier for a specific version of a resource, often a message digest.

For example: `ETag: "737060cd8c284d8af7ad3082f209582d"`

## Expires

[RFC 9111, permanent] Gives the date/time after which the response is considered stale (in "HTTP-date" format as defined by RFC 9110).

For example: `Expires: Thu, 01 Dec 1994 16:00:00 GMT`

## IM

[RFC 3229, permanent] Instance-manipulations applied to the response.

For example: `IM: feed`

## Last-Modified

[RFC 9110, permanent] The last modified date for the requested object (in "HTTP-date" format as defined by RFC 9110).

For example: `Last-Modified: Tue, 15 Nov 1994 12:45:26 GMT`

## Link

[RFC 8288, permanent] Used to express a typed relationship with another resource, where the relation type is defined by RFC 8288.[51]

For example: `Link: </feed>; rel="alternate"`

## Location

[RFC 9110, permanent] Used in redirection, or when a new resource has been created.

For example: `Location: http://www.w3.org/pub/WWW/People.html`

For example: `Location: /pub/WWW/People.html`

## P3P

[RFC 2626, permanent] This field is supposed to set P3P policy, in the form of P3P:CP="your_compact_policy". However, P3P did not take off,[52] most browsers have never fully implemented it; a lot of websites set this field with fake policy text, enough to fool browsers into thinking a P3P policy existed and granting permissions for third party cookies.

For example: `P3P: CP="This is not a P3P policy! See https://en.wikipedia.org/wiki/Special:CentralAutoLogin/P3P for more info."`

## Pragma

[RFC 9111, permanent] Implementation-specific fields that may have various effects anywhere along the request-response chain.

For example: `Pragma: no-cache`

## Preference-Applied

[RFC 7240, permanent] Indicates which Prefer tokens were honored by the server and applied to the processing of the request.

For example: `Preference-Applied: return=representation`

## Proxy-Authenticate

[RFC 9110, permanent] Request authentication to access the proxy.

For example: `Proxy-Authenticate: Basic`

## Public-Key-Pins

[RFC 7469, permanent] HTTP Public Key Pinning, announces hash of website's authentic TLS certificate.

For example: `Public-Key-Pins: max-age=2592000; pin-sha256="E9CZ9INDbd+2eRQozYqqbQ2yXLVKB9+xcprMF+44U1g=";`

## Retry-After

[RFC 9110, permanent] If an entity is temporarily unavailable, this instructs the client to try again later. Value could be a specified period of time (in seconds) or a HTTP-date.

For example 1: `Retry-After: 120` For example 2: `Retry-After: Fri, 07 Nov 2014 23:59:59 GMT`

## Server

[RFC 9110, permanent] A name for the server.

For example: `Server: Apache/2.4.1 (Unix)`

## Set-Cookie

[RFC 6265, permanent] An HTTP cookie.

For example: `Set-Cookie: CookieName=CookieValue; Max-Age=3600; Version=1`

## Strict-Transport-Security

[RFC 6797, permanent] A HSTS Policy informing the HTTP client how long to cache the HTTPS-only policy and whether this applies to subdomains.

For example: `Strict-Transport-Security: max-age=16070400; includeSubDomains`

## Trailer

[RFC 9110, permanent] The Trailer general field value indicates that the given set of header fields is present in the trailer of a message encoded with chunked transfer coding.

For example: `Trailer: Max-Forwards`

## Transfer-Encoding

[RFC 9110, permanent] The form of encoding used to safely transfer the entity to the user. Currently defined methods are: chunked, compress, deflate, gzip, identity. Must not be used with HTTP/2.

For example: `Transfer-Encoding: chunked`

## Tk

[RFC 2295, permanent] Tracking Status header, value suggested to be sent in response to a DNT (do-not-track) request. Possible values:

    "!" — under construction
    "?" — dynamic
    "G" — gateway to multiple parties
    "N" — not tracking
    "T" — tracking
    "C" — tracking with consent
    "P" — tracking only if consented
    "D" — disregarding DNT
    "U" — updated

For example: `Tk: ?`

## Upgrade

[RFC 9110, permanent] Ask the client to upgrade to another protocol. Must not be used in HTTP/2.

For example: `Upgrade: h2c, HTTPS/1.3, IRC/6.9, RTA/x11, websocket`

## Vary

[RFC 9110, permanent] Tells downstream proxies how to match future request headers to decide whether the cached response can be used rather than requesting a fresh one from the origin server.

For example 1: `Vary: *` For example 2: `Vary: Accept-Language`

## Via

[RFC 9110, permanent] Informs the client of proxies through which the response was sent.

For example: `Via: 1.0 fred, 1.1 example.com (Apache/1.1)`

## Warning

[RFC 7234, RFC 9111, obsolete] A general warning about possible problems with the entity body.

For example: `Warning: 199 Miscellaneous warning`

## WWW-Authenticate

[RFC 9110, permanent] Indicates the authentication scheme that should be used to access the requested entity.

For example: `WWW-Authenticate: Basic`

## X-Frame-Options

[RFC 7034, obsolete] Clickjacking protection: deny - no rendering within a frame, sameorigin - no rendering if origin mismatch, allow-from - allow from specified location, allowall - non-standard, allow from any location.

For example: `X-Frame-Options: deny`

# Common non-standard response fields
## Content-Security-Policy, X-Content-Security-Policy, X-WebKit-CSP

Content Security Policy definition.

For example: `X-WebKit-CSP: default-src 'self'`

## Expect-CT

Notify to prefer to enforce Certificate Transparency.

For example: `Expect-CT: max-age=604800, enforce, report-uri="https://example.example/report"`

## NEL

Used to configure network request logging.

For example: `NEL: { "report_to": "name_of_reporting_group", "max_age": 12345, "include_subdomains": false, "success_fraction": 0.0, "failure_fraction": 1.0 }`

## Permissions-Policy

To allow or disable different features or APIs of the browser.

For example: `Permissions-Policy: fullscreen=(), camera=(), microphone=(), geolocation=(), interest-cohort=()`

## Refresh

Tells the browser to refresh the page or redirect to a different URL, either after a given number of seconds (0 meaning immediately), or when a new resource has been created.[clarification needed] Introduced by Netscape in 1995 and has since become a de facto standard supported by most web browsers. Was eventually standardized in the HTML Living Standard in 2017.

For example: `Refresh: 5; url=http://www.w3.org/pub/WWW/People.html`

## Report-To

Instructs the user agent to store reporting endpoints for an origin.

For example: `Report-To: { "group": "csp-endpoint", "max_age": 10886400, "endpoints": [ { "url": "https-url-of-site-which-collects-reports" } ] }`

## Status

CGI header field specifying the status of the HTTP response. Normal HTTP responses use a separate "Status-Line" instead, defined by RFC 9110.

For example: `Status: 200 OK`

## Timing-Allow-Origin

The Timing-Allow-Origin response header specifies origins that are allowed to see values of attributes retrieved via features of the Resource Timing API, which would otherwise be reported as zero due to cross-origin restrictions.

For example: `Timing-Allow-Origin: *`

## X-Content-Duration

Provide the duration of the audio or video in seconds. Not supported by current browsers – the header was only supported by Gecko browsers, from which support was removed in 2015.

For example: `X-Content-Duration: 42.666`

## X-Content-Type-Options

The only defined value, "nosniff", prevents Internet Explorer from MIME-sniffing a response away from the declared content-type. This also applies to Google Chrome, when downloading extensions.

For example: `X-Content-Type-Options: nosniff`

## X-Powered-By

Specifies the technology (e.g. ASP.NET, PHP, JBoss) supporting the web application (version details are often in X-Runtime, X-Version, or X-AspNet-Version).

For example: `X-Powered-By: PHP/5.4.0`

## X-Redirect-By

Specifies the component that is responsible for a particular redirect.

For example: `X-Redirect-By: WordPress`
`X-Redirect-By: Polylang`
`X-Request-ID, X-Correlation-ID`

Correlates HTTP requests between a client and server.

For example: `X-Request-ID: f058ebd6-02f7-4d3f-942e-904344e8cde5`

## X-UA-Compatible

Recommends the preferred rendering engine (often a backward-compatibility mode) to use to display the content. Also used to activate Chrome Frame in Internet Explorer. In HTML Standard, only the IE=edge value is defined.

For example:
```
X-UA-Compatible: IE=edge
X-UA-Compatible: IE=EmulateIE7
X-UA-Compatible: Chrome=1
X-XSS-Protection
```

## Cross-site scripting (XSS) filter

For example: `X-XSS-Protection: 1; mode=block`
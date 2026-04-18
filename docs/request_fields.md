# Standard request fields
## A-IM

[RFC 3229, permanent] Acceptable instance-manipulations for the request.

For example: `A-IM: feed`

## Accept

[RFC 9110, permanent] Media type(s) that is/are acceptable for the response. See Content negotiation.

For example: `Accept: text/html`

## Accept-Charset

[RFC 9110, permanent] Character sets that are acceptable.

For example: `Accept-Charset: utf-8`

## Accept-Datetime

[RFC 7089, provisional] Acceptable version in time.

For example: `Accept-Datetime: Thu, 31 May 2007 20:35:00 GMT`

## Accept-Encoding

[RFC 9110, permanent] List of acceptable encodings. See HTTP compression.

For example: `Accept-Encoding: gzip, deflate`

## Accept-Language

[RFC 9110, permanent] List of acceptable human languages for response. See Content negotiation.

For example: Accept-Language: `en-US`

## Access-Control-Request-Method, Access-Control-Request-Headers

[permanent] Initiates a request for cross-origin resource sharing with Origin (below).

For example: `Access-Control-Request-Method: GET`

## Authorization

[RFC 9110, permanent] Authentication credentials for HTTP authentication.

For example: `Authorization: Basic QWxhZGRpbjpvcGVuIHNlc2FtZQ==`

## Cache-Control

[RFC 9111, permanent] Used to specify directives that must be obeyed by all caching mechanisms along the request-response chain. Per HTTP/1.1, the no-cache value allows the browser to tell the server and intermediate caches that it wants a fresh version of the resource. The HTTP/1.0, Pragma: no-cache header field has the same purpose.

The behavior of Pragma: no-cache in a response is not specified yet some user agents support it. HTTP/1.1 specifically warns against relying on this behavior.

For example: `Cache-Control: no-cache`

## Connection

[RFC 9110, permanent] Control options for the current connection and list of hop-by-hop request fields. Must not be used with HTTP/2.

For example: `Connection: keep-alive Connection: Upgrade`

## Content-Encoding

[RFC 9110, permanent] The type of encoding used on the data. See HTTP compression.

For example: `Content-Encoding: gzip`

## Content-Length

[RFC 9110, permanent] The length of the request body in octets (8-bit bytes).

For example: `Content-Length: 348`

## Content-MD5

[RFC 1544, 1864, 4021, obsolete] A Base64-encoded binary MD5 sum of the content of the request body.

For example: `Content-MD5: Q2hlY2sgSW50ZWdyaXR5IQ==`

## Content-Type

[RFC 9110, permanent] The Media type of the body of the request (used with POST and PUT requests).

For example: `Content-Type: application/x-www-form-urlencoded`

## Cookie

[RFC 2965, 6265, permanent] An HTTP cookie previously sent by the server with Set-Cookie (below).

For example: `Cookie: $Version=1; Skin=new;`

## Date

[RFC 9110, permanent] The date and time at which the message was originated (in "HTTP-date" format as defined by RFC 9110: HTTP Semantics, section 5.6.7 "Date/Time Formats").

For example: `Date: Tue, 15 Nov 1994 08:12:31 GMT`

## Expect

[RFC 9110, permanent] Indicates that particular server behaviors are required by the client.

For example: `Expect: 100-continue`

## Forwarded

[RFC 7239, permanent] Disclose original information of a client connecting to a web server through an HTTP proxy.

For example: `Forwarded: for=192.0.2.60;proto=http;by=203.0.113.43 Forwarded: for=192.0.2.43, for=198.51.100.17`

## From

[RFC 9110, permanent] The email address of the user making the request.

For example: `From: user@example.com`

## Host

[RFC 9110, 9113, permanent] The domain name of the server (for virtual hosting), and the TCP port number on which the server is listening. The port number may be omitted if the port is the standard port for the service requested. Mandatory since HTTP/1.1. If the request is generated directly in HTTP/2, it should not be used.

For example: `Host: en.wikipedia.org:8080 Host: en.wikipedia.org`

## HTTP2-Settings

[RFC 7540, 9113, obsolete] A request that upgrades from HTTP/1.1 to HTTP/2 MUST include exactly one HTTP2-Settings header field. The HTTP2-Settings header field is a connection-specific header field that includes parameters that govern the HTTP/2 connection, provided in anticipation of the server accepting the request to upgrade.

For example: `HTTP2-Settings: token64`

## If-Match

[RFC 9110, permanent] Only perform the action if the client supplied entity matches the same entity on the server. This is mainly for methods like PUT to only update a resource if it has not been modified since the user last updated it.

For example: `If-Match: "737060cd8c284d8af7ad3082f209582d"`

## If-Modified-Since

[RFC 9110, permanent] Allows a 304 Not Modified to be returned if content is unchanged.

For example: `If-Modified-Since: Sat, 29 Oct 1994 19:43:31 GMT`

## If-None-Match

[RFC 9110, permanent] Allows a 304 Not Modified to be returned if content is unchanged, see HTTP ETag.

For example: `If-None-Match: "737060cd8c284d8af7ad3082f209582d"`

## If-Range

[RFC 9110, permanent] If the entity is unchanged, send me the part(s) that I am missing; otherwise, send me the entire new entity.

For example: `If-Range: "737060cd8c284d8af7ad3082f209582d"`

## If-Unmodified-Since

[RFC 9110, permanent] Only send the response if the entity has not been modified since a specific time.

For example: `If-Unmodified-Since: Sat, 29 Oct 1994 19:43:31 GMT`

## Max-Forwards

[RFC 9110, permanent] Limit the number of times the message can be forwarded through proxies or gateways.

For example: `Max-Forwards: 10`

## Origin

[RFC 6454, permanent] Initiates a request for cross-origin resource sharing (asks server for Access-Control-* response fields).

For example: `Origin: http://www.example-social-network.com`

## Pragma

[RFC 9111, outdated] Implementation-specific fields that may have various effects anywhere along the request-response chain.

For example: `Pragma: no-cache`

## Prefer

[RFC 7240, permanent] Allows client to request that certain behaviors be employed by a server while processing a request.

For example: `Prefer: return=representation`

## Proxy-Authorization

[RFC 9110, permanent] Authorization credentials for connecting to a proxy.

For example: `Proxy-Authorization: Basic QWxhZGRpbjpvcGVuIHNlc2FtZQ==`

## Range

[RFC 9110, permanent] Request only part of an entity. Bytes are numbered from 0. See Byte serving.

For example: `Range: bytes=500-999`

## Referer

[RFC 9110, permanent] The address of the previous web page from which a link to the currently requested page was followed.

Although the intended term is actually spelled "referrer", the misspelling is in the RFC as well as in most implementations, and is therefore considered correct terminology.

For example: `Referer: http://en.wikipedia.org/wiki/Main_Page`

## TE

[RFC 9110, permanent] The transfer encodings the user agent is willing to accept: the same values as for the response header field Transfer-Encoding can be used, plus the "trailers" value (related to the "chunked" transfer method) to notify the server it expects to receive additional fields in the trailer after the last, zero-sized, chunk. Only trailers is supported in HTTP/2.

For example: `TE: trailers, deflate`

## Trailer

[RFC 9110, permanent] The Trailer general field value indicates that the given set of header fields is present in the trailer of a message encoded with chunked transfer coding.

For example: `Trailer: Max-Forwards`

## Transfer-Encoding

[RFC 9110, permanent] The form of encoding used to safely transfer the entity to the user. Currently defined methods are: chunked, compress, deflate, gzip, identity. Must not be used with HTTP/2.

For example: `Transfer-Encoding: chunked`

## User-Agent

[RFC 9110, permanent] The user agent string of the user agent.

For example: `User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/12.0`

## Upgrade

[RFC 9110, permanent] Ask the server to upgrade to another protocol. Must not be used in HTTP/2.

For example: `Upgrade: h2c, HTTPS/1.3, IRC/6.9, RTA/x11, websocket`

## Via

[RFC 9110, permanent] Informs the server of proxies through which the request was sent.

For example: `Via: 1.0 fred, 1.1 example.com (Apache/1.1)`

## Warning

[RFC 7234, 9111, obsolete] A warning about a possible problem with the entity body. Since this header is often neither sent by servers nor acknowledged by clients, this header and its codes were obsoleted by the HTTP Working Group in 2022 with RFC 9111.

The following caching related warning codes were specified under RFC 7234.

110 Response is Stale
    The response provided by a cache is stale (the content's age exceeds a maximum age set by a Cache-Control header or heuristically chosen lifetime).

111 Revalidation Failed
    The cache was unable to validate the response, due to an inability to reach the origin server.

112 Disconnected Operation
    The cache is intentionally disconnected from the rest of the network.

113 Heuristic Expiration
    The cache heuristically chose a freshness lifetime greater than 24 hours and the response's age is greater than 24 hours.

199 Miscellaneous Warning
    Arbitrary, non-specific warning. The warning text may be logged or presented to the user.

214 Transformation Applied
    Added by a proxy if it applies any transformation to the representation, such as changing the content encoding, media type or the like.

299 Miscellaneous Persistent Warning
    Same as 199, but indicating a persistent warning.

For example: `Warning: 199 Miscellaneous warning`

# Common non-standard request fields
## Upgrade-Insecure-Requests

Tells a server which (presumably in the middle of a HTTP -> HTTPS migration) hosts mixed content that the client would prefer redirection to HTTPS and can handle Content-Security-Policy: upgrade-insecure-requests

For example: `Upgrade-Insecure-Requests: 1`

## X-Requested-With

Mainly used to identify Ajax requests (most JavaScript frameworks send this field with value of XMLHttpRequest); this also identifies Android apps using WebView.

For example: `X-Requested-With: XMLHttpRequest`

## DNT

Requests a web application to disable their tracking of a user. This is Mozilla's version of the X-Do-Not-Track header field (since Firefox 4.0 Beta 11). Safari and IE9 also have support for this field. On March 7, 2011, a draft proposal was submitted to IETF. The W3C Tracking Protection Working Group is producing a specification.

For example:

`DNT: 1` (Do Not Track Enabled)

`DNT: 0` (Do Not Track Disabled)

## X-Forwarded-For

A de facto standard for identifying the originating IP address of a client connecting to a web server through an HTTP proxy or load balancer. Superseded by Forwarded header.

For example: `X-Forwarded-For: client1, proxy1, proxy2 X-Forwarded-For: 129.78.138.66, 129.78.64.103`

## X-Forwarded-Host

A de facto standard for identifying the original host requested by the client in the Host HTTP request header, since the host name and/or port of the reverse proxy (load balancer) may differ from the origin server handling the request. Superseded by Forwarded header.

For example:

X-Forwarded-Host: `en.wikipedia.org:8080`

X-Forwarded-Host: `en.wikipedia.org`

## X-Forwarded-Proto

A de facto standard for identifying the originating protocol of an HTTP request, since a reverse proxy (or a load balancer) may communicate with a web server using HTTP even if the request to the reverse proxy is HTTPS. An alternative form of the header (X-ProxyUser-Ip) is used by Google clients talking to Google servers. Superseded by Forwarded header.

For example: `X-Forwarded-Proto: https`

## Front-End-Https

Non-standard header field used by Microsoft applications and load-balancers.

For example: `Front-End-Https: on`

## X-Http-Method-Override

Requests a web application to override the method specified in the request (typically POST) with the method given in the header field (typically PUT or DELETE). This can be used when a user agent or firewall prevents PUT or DELETE methods from being sent directly (this is either a bug in the software component, which ought to be fixed, or an intentional configuration, in which case bypassing it may be the wrong thing to do).

For example: `X-HTTP-Method-Override: DELETE`

## X-ATT-DeviceId

Allows easier parsing of the MakeModel/Firmware that is usually found in the User-Agent String of AT&T Devices.

For example: `X-Att-Deviceid: GT-P7320/P7320XXLPG`

## X-Wap-Profile

Links to an XML file on the Internet with a full description and details about the device currently connecting. In the example to the right is an XML file for an AT&T Samsung Galaxy S2.

For example: `x-wap-profile: http://wap.samsungmobile.com/uaprof/SGH-I777.xml`

## Proxy-Connection

Implemented as a misunderstanding of the HTTP specifications. Common because of mistakes in implementations of early HTTP versions. Has exactly the same functionality as standard Connection field. Must not be used with HTTP/2.

For example: `Proxy-Connection: keep-alive`

## X-UIDH

Server-side deep packet inspection of a unique ID identifying customers of Verizon Wireless; also known as "perma-cookie" or "supercookie".

For example: `X-UIDH: ...`

## X-Csrf-Token

Used to prevent cross-site request forgery. Alternative header names are: X-CSRFToken and X-XSRF-TOKEN.

For example: `X-Csrf-Token: i8XNjC4b8KVok4uw5RftR38Wgp2BFwql`

## X-Request-ID, X-Correlation-ID, Correlation-ID

Correlates HTTP requests between a client and server. Superseded by the traceparent header.

For example: `X-Request-ID: f058ebd6-02f7-4d3f-942e-904344e8cde5`

## Save-Data

The Save-Data client hint request header available in Chrome, Opera, and Yandex browsers lets developers deliver lighter, faster applications to users who opt-in to data saving mode in their browser.

For example: `Save-Data: on`

## Sec-GPC

The Sec-GPC (Global Privacy Control) request header indicates whether the user consents to a website or service selling or sharing their personal information with third parties.

For example: `Sec-GPC: 1`
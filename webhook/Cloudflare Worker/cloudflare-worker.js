addEventListener('fetch', event => {
    event.respondWith(incoming(event.request));
});

async function incoming(request) {
    // Log what we just received
    console.log('Received request. Post data: ' + await request.text());

    // 'X-Viber-Content-Signature' needs to be in the header of the request
    if (!request.headers.get('X-Viber-Content-Signature')) {
        // Respond with 403 if not
        return new Response(null, {status: 403});
    }

    // Respond with 200
    return new Response(null, {status: 200});
}